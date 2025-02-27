
import numpy as np
import math



class Ped:
    def __init__(self, type: str, direction: str, params):
        super().__init__()
        self.x = 0
        self.y = 0
        self.type = type # one of {"ped", "wheelchair", "crutches_user", "child", "elder"}
        self.direction = direction # one of {"left2right", "right2left"}
        self.speed = self.set_speed(type, params)
        self.radius_standing = params.radius_of_space_occupied_when_standing[type]
        self.radius_moving = params.radius_of_space_occupied_when_moving[type]
        self.radius_moving_curr_step = self.radius_moving
        self.status = "standing" # one of {"standing", "moving", "finished"}

        self.previousx = 0
        self.previousy = 0
        self.nomove_counter = 0
        self.smallmove_counter = 0

        self.set_initial_standing_position(params)
        


    def set_speed(self, type, params) -> int:
        if type == "ped":
            return np.random.normal(params.ped_walking_speed_mean, params.ped_walking_speed_sigma, 1)[0]
        elif type == "wheelchair":
            return np.random.normal(params.wheelchair_rolling_speed_mean, params.wheelchair_rolling_speed_sigma, 1)[0]
        elif type == "crutches_user":
            return np.random.normal(params.crutches_user_walking_speed_mean, params.crutches_user_walking_speed_sigma, 1)[0]
        elif type == "child":
            return np.random.normal(params.children_walking_speed_mean, params.children_walking_speed_sigma, 1)[0]
        elif type == "elder":
            return np.random.normal(params.elder_walking_speed_mean, params.elder_walking_speed_sigma, 1)[0]

    def set_initial_standing_position(self, params):
        is_conflict = True
        newx = 0
        newy = 0
        while is_conflict:
            x_offset = abs(np.random.normal(params.waiting_area_position_x_offset_mean, params.waiting_area_position_x_offset_sigma, 1)[0])
            if self.direction == "left2right":
                newx = params.waiting_area_length - x_offset
            elif self.direction == "right2left":
                newx = params.waiting_area_length + params.crosswalk_length + x_offset
            newy = np.random.normal(params.waiting_area_position_y_mean, params.waiting_area_position_y_sigma, 1)[0]
            if newx < 0 or newx > params.waiting_area_length + params.crosswalk_length + params.waiting_area_length: # outside, so drop
                is_conflict = True
                continue

            #check whether conflict with existing params.all_peds_lr or params.all_peds_rl
            if self.direction == "left2right":
                if not self.is_newposition_conflicted(newx, newy, 0, "standing", params):
                    is_conflict = False
            elif self.direction == "right2left":
                if not self.is_newposition_conflicted(newx, newy, 0, "standing", params):
                    is_conflict = False
        
        self.x = newx
        self.y = newy

    def is_y_inside_bound(self, newy, params) -> bool:
        if newy > params.crosswalk_width + params.outside_margin_width or newy < - params.outside_margin_width:
            return False
        return True

    def is_inside_crosswalk(self, params) -> bool:        
        if (self.x >= params.waiting_area_length and self.x <= params.waiting_area_length+params.crosswalk_length) and (self.y >= 0 and self.y <= params.crosswalk_width):
            return True
        return False

    def is_newposition_conflicted(self, newx: int, newy: int, real_radius, mode: str, params) -> bool:
        # real_radius is only useful when mode=="moving"
        used_all_peds = 0
        if mode == "standing":
            if self.direction == "left2right":
                used_all_peds = params.all_peds_lr 
            elif self.direction == "right2left":
                used_all_peds = params.all_peds_rl 
        if mode == "moving":
            used_all_peds = params.all_peds
        
        for another in used_all_peds:
            if mode == "moving" and (another.status == "finished"):
                continue
            if another.status == self.status and another.x == self.x and another.y == self.y and another.direction == self.direction and another.speed == self.speed:
                continue
            if "debug" in params.log_keywords: print("is_newposition_conflicted another: ", another.status)
            distance = math.sqrt((newx - another.x)**2 + (newy - another.y)**2)
            radius_sum = 0
            if mode == "standing":
                radius_sum = self.radius_standing + another.radius_standing
            elif mode == "moving":
                radius_sum = real_radius + another.radius_moving_curr_step
            if "debug" in params.log_keywords: print("curr: ", self.x, " ", self.y, " another: ", another.x, " ", another.y)
            if "debug" in params.log_keywords: print("radius_sum: ", radius_sum, " distance: ", distance)
            if (distance < radius_sum):
                return True
        return False

    def generate_100_newpositions(self, params, counter):
        offset = self.speed * params.step_time / 100
        all_newpositions_andcounter = list()

        circle_radius = self.speed * params.step_time - offset * counter
        farthest_newx = (self.x + circle_radius ) if self.direction == "left2right" else (self.x - circle_radius )
        farthest_newy = self.y
        all_newpositions_andcounter.append([farthest_newx, farthest_newy, self.radius_moving])
        if "debug_100newpos" in params.log_keywords: print("-----------\nfarthest_newx, farthest_newy:  ",  farthest_newx, farthest_newy)

        for i in range(1, 99 - counter):
            newx = farthest_newx - offset * i if self.direction == "left2right" else farthest_newx + offset * i
            circle_radius_sq = circle_radius ** 2
            x_x0_sq = (newx - self.x)**2
            if "debug_100newpos" in params.log_keywords: 
                print("-----------\ncounter: ", counter)
                print("newx : ", newx, " self.x: ", self.x )
                print("circle_radius : ", circle_radius )
                print("circle_radius_sq : ", circle_radius_sq )
                print("x_x0_sq: ",  x_x0_sq)
                print("circle_radius_sq - x_x0_sq: ", circle_radius_sq - x_x0_sq)
            if circle_radius_sq - x_x0_sq < 0: # this case is weired and should not happen in theory but it happens rarely. Guess it is becuase precision error.
                continue
            sqrt_abs = math.sqrt(circle_radius_sq - x_x0_sq)
            newy1 = sqrt_abs + self.y
            newy2 = 0 - sqrt_abs + self.y
            if "debug_100newpos" in params.log_keywords: 
                print("sqrt_abs: ", sqrt_abs, " self.y: ", self.y)
                print("newy1: ", newy1, " newy2: ", newy2)

            if self.direction == "left2right":
                if self.is_y_inside_bound(newy2, params): all_newpositions_andcounter.append([newx, newy2, counter])#throw thoes outside bound
                if self.is_y_inside_bound(newy1, params): all_newpositions_andcounter.append([newx, newy1, counter])
            else:
                if self.is_y_inside_bound(newy1, params): all_newpositions_andcounter.append([newx, newy1, counter])
                if self.is_y_inside_bound(newy2, params): all_newpositions_andcounter.append([newx, newy2, counter])
        return all_newpositions_andcounter


    def generate_100_pos_to_move_into_bounds(self, params):
        # move into bounds if outside bounds

        one_step_distance = self.speed * params.step_time 
        all_newpositions_and_ctr = list()

        tan_result = 0
        if self.direction == "left2right" and self.x < params.crosswalk_length and self.y < - params.outside_margin_width:
            # left-bottom corner
            tan_result = abs(- params.outside_margin_width - self.y) / abs(params.waiting_area_length - self.x)
        elif self.direction == "left2right" and self.x < params.crosswalk_length and self.y > params.crosswalk_width + params.outside_margin_width:
            # left-top corner
            tan_result = abs(params.crosswalk_width + params.outside_margin_width - self.y) / abs(params.waiting_area_length - self.x)
        elif self.direction == "right2left" and self.x > params.waiting_area_length+params.crosswalk_length and self.y < - params.outside_margin_width:
            # right-bottom corner
            tan_result = abs(- params.outside_margin_width - self.y) / abs(params.waiting_area_length+params.crosswalk_length - self.x)
        elif self.direction == "right2left" and self.x > params.waiting_area_length+params.crosswalk_length and self.y > params.crosswalk_width + params.outside_margin_width:
            # right-top corner
            tan_result = abs(params.crosswalk_width + params.outside_margin_width - self.y) / abs(params.waiting_area_length+params.crosswalk_length - self.x)
        
        slope_radian = math.atan(tan_result) 
        x_max_move_distance = math.cos(slope_radian) * one_step_distance
        offset = x_max_move_distance / 100
        counter = 0
        while counter >= 0 and counter < 100:
            x_curr_move_distance = x_max_move_distance - offset * counter
            newx = (self.x + x_curr_move_distance) if self.direction == "left2right" else (self.x - x_curr_move_distance) 
            newy = self.y
            if self.y < - params.outside_margin_width:
                newy = self.y + x_curr_move_distance * tan_result 
            if self.y > params.crosswalk_width + params.outside_margin_width:
                newy = self.y - x_curr_move_distance * tan_result 
            all_newpositions_and_ctr.append([newx, newy, counter])
            counter += 1
        return all_newpositions_and_ctr
            



    def move_one_step(self, params):
        # when finish
        if self.direction == "left2right" and self.x > params.crosswalk_length + params.waiting_area_length:
            self.status = "finished"
            return
        if self.direction == "right2left" and self.x < params.waiting_area_length:
            self.status = "finished"
            return


        # move forward one step
        self.previousx = self.x
        self.previousy = self.y
        counter = 0
        while counter >= 0 and counter < 100:
            all_newpositions = list()
            need2_move_into_bound = False
            if not self.is_y_inside_bound(self.y, params) and ( self.x < params.crosswalk_length or self.x > params.waiting_area_length+params.crosswalk_length ):
                need2_move_into_bound = True
                all_newpositions = self.generate_100_pos_to_move_into_bounds(params)
            else:
                all_newpositions = self.generate_100_newpositions(params, counter)
            if "debug" in params.log_keywords: 
                for newx, newy, _ in all_newpositions:
                    print("all_newpositions pos: ", newx, newy, " counter: ", counter)
            for newx, newy, new_pos_id_when_move_into_bound in all_newpositions:
                if need2_move_into_bound:
                    real_occupied_area_radius = self.radius_moving - ( (self.radius_moving - self.radius_standing)/100 ) * new_pos_id_when_move_into_bound
                else:
                    real_occupied_area_radius = self.radius_moving - ( (self.radius_moving - self.radius_standing)/100 ) * counter
                if not self.is_newposition_conflicted(newx, newy, real_occupied_area_radius, "moving", params):
                    if "debug" in params.log_keywords: print("\nFOUND!!\nold pos: ", self.x, self.y)
                    self.x = newx
                    self.y = newy
                    self.status = "moving" # move as designed
                    if abs(newx - self.previousx) <= abs(self.speed * params.step_time * 0.1):
                        self.smallmove_counter += 1
                    else:
                        self.smallmove_counter = 0
                    self.nomove_counter = 0
                    self.radius_moving_curr_step = real_occupied_area_radius
                    if "debug" in params.log_keywords: 
                        print("newx newy: ", newx, newy)
                        print("new pos: ", newx, newy)
                    return
            counter += 1
            if need2_move_into_bound: break # only 1 round of 100 new position for need2_move_into_bound
            
        self.status = "moving" #  no place to move so stay
        self.nomove_counter += 1


    
