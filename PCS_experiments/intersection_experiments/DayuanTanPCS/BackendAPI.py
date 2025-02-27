import backend.Ped as Ped
from backend.Utilities import Utilities as Utilities
from backend.Circles import Circles as Circles

import operator
import global_params.global_params as global_params

class BackendAPI:
    @staticmethod
    def set_peds_initial_positions(params):
        #
        # Initial
        #
        

        if "core" in params.log_keywords:
            print("Parameters applied!\ncrosswalk_width: ", params.crosswalk_width)
            print("crosswalk_length: ", params.crosswalk_length)


        for i in range(0, params.ped_amount_lr):
            params.all_peds_lr.append(Ped.Ped("ped", "left2right", params))
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_lr[i].direction, " Coor: ", params.all_peds_lr[i].x, params.all_peds_lr[i].y, params.all_peds_lr[i].type, params.all_peds_lr[i].speed)
        for i in range(0, params.wheelchair_amount_lr):
            params.all_peds_lr.append(Ped.Ped("wheelchair", "left2right", params))
            curr_ctr = params.ped_amount_lr
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_lr[i+curr_ctr].direction, " Coor: ", params.all_peds_lr[i+curr_ctr].x, params.all_peds_lr[i+curr_ctr].y, params.all_peds_lr[i+curr_ctr].type, params.all_peds_lr[i+curr_ctr].speed)
        for i in range(0, params.crutches_user_amount_lr):
            params.all_peds_lr.append(Ped.Ped("crutches_user", "left2right", params))
            curr_ctr = params.ped_amount_lr + params.wheelchair_amount_lr
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_lr[i+curr_ctr].direction, " Coor: ", params.all_peds_lr[i+curr_ctr].x, params.all_peds_lr[i+curr_ctr].y, params.all_peds_lr[i+curr_ctr].type, params.all_peds_lr[i+curr_ctr].speed)
        for i in range(0, params.children_amount_lr):
            params.all_peds_lr.append(Ped.Ped("child", "left2right", params))
            curr_ctr = params.ped_amount_lr + params.wheelchair_amount_lr + params.crutches_user_amount_lr
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_lr[i+curr_ctr].direction, " Coor: ", params.all_peds_lr[i+curr_ctr].x, params.all_peds_lr[i+curr_ctr].y, params.all_peds_lr[i+curr_ctr].type, params.all_peds_lr[i+curr_ctr].speed)
        for i in range(0, params.elder_amount_lr):
            params.all_peds_lr.append(Ped.Ped("elder", "left2right", params))
            curr_ctr = params.ped_amount_lr + params.wheelchair_amount_lr + params.crutches_user_amount_lr + params.children_amount_lr
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_lr[i+curr_ctr].direction, " Coor: ", params.all_peds_lr[i+curr_ctr].x, params.all_peds_lr[i+curr_ctr].y, params.all_peds_lr[i+curr_ctr].type, params.all_peds_lr[i+curr_ctr].speed)

        for i in range(0, params.ped_amount_rl):
            params.all_peds_rl.append(Ped.Ped("ped", "right2left", params))
            curr_ctr = 0
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_rl[i+curr_ctr].direction, " Coor: ", params.all_peds_rl[i+curr_ctr].x, params.all_peds_rl[i+curr_ctr].y, params.all_peds_rl[i+curr_ctr].type, params.all_peds_rl[i+curr_ctr].speed)
        for i in range(0, params.wheelchair_amount_rl):
            params.all_peds_rl.append(Ped.Ped("wheelchair", "right2left", params))
            curr_ctr = params.ped_amount_rl
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_rl[i+curr_ctr].direction, " Coor: ", params.all_peds_rl[i+curr_ctr].x, params.all_peds_rl[i+curr_ctr].y, params.all_peds_rl[i+curr_ctr].type, params.all_peds_rl[i+curr_ctr].speed)
        for i in range(0, params.crutches_user_amount_rl):
            params.all_peds_rl.append(Ped.Ped("crutches_user", "right2left", params))
            curr_ctr = params.ped_amount_rl + params.wheelchair_amount_rl
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_rl[i+curr_ctr].direction, " Coor: ", params.all_peds_rl[i+curr_ctr].x, params.all_peds_rl[i+curr_ctr].y, params.all_peds_rl[i+curr_ctr].type, params.all_peds_rl[i+curr_ctr].speed)
        for i in range(0, params.children_amount_rl):
            params.all_peds_rl.append(Ped.Ped("child", "right2left", params))
            curr_ctr = params.ped_amount_rl + params.wheelchair_amount_rl + params.crutches_user_amount_rl
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_rl[i+curr_ctr].direction, " Coor: ", params.all_peds_rl[i+curr_ctr].x, params.all_peds_rl[i+curr_ctr].y, params.all_peds_rl[i+curr_ctr].type, params.all_peds_rl[i+curr_ctr].speed)
        for i in range(0, params.elder_amount_rl):
            params.all_peds_rl.append(Ped.Ped("elder", "right2left", params))
            curr_ctr = params.ped_amount_rl + params.wheelchair_amount_rl + params.crutches_user_amount_rl + params.children_amount_rl
            if "debug" in params.log_keywords: print("Direc: ",  params.all_peds_rl[i+curr_ctr].direction, " Coor: ", params.all_peds_rl[i+curr_ctr].x, params.all_peds_rl[i+curr_ctr].y, params.all_peds_rl[i+curr_ctr].type, params.all_peds_rl[i+curr_ctr].speed)


        params.all_peds = params.all_peds_lr + params.all_peds_rl

        total_size_lr = params.ped_amount_lr + params.wheelchair_amount_lr + params.crutches_user_amount_lr + params.children_amount_lr + params.elder_amount_lr
        total_size_rl = params.ped_amount_rl + params.wheelchair_amount_rl + params.crutches_user_amount_rl + params.children_amount_rl + params.elder_amount_rl
        total_size =  total_size_lr + total_size_rl
        if "debug" in params.log_keywords: print("total_size_lr: ", total_size_lr )
        if "debug" in params.log_keywords: print("total_size_rl: ", total_size_rl )
        if "debug" in params.log_keywords: print("total_size: ", total_size, " len(all_peds): ", len(params.all_peds))
        if total_size != len(params.all_peds):
            raise Exception("total_size != len(all_peds)")

        # order
        BackendAPI.order_peds_leftright_inturn(params)
        

        if "core" in params.log_keywords: print("\nAll pedestrians have been set up their initial standing positions!\n")
        if "plot" in params.log_keywords: Utilities.plot_positions(params, "standing")

    @staticmethod
    def order_peds_leftright_inturn(params):
        #
        # order peds, update params.all_peds_ordered to: [lr_no1, rl_no1, lr_no2, rl_no2, ...]
        #

        # all_peds_sorted_by_x = sorted(all_peds, key=operator.attrgetter('y'), reverse=True)
        params.all_peds_lr_sorted_by_x = sorted(params.all_peds_lr, key=operator.attrgetter('x'), reverse=True)
        if "debug" in params.log_keywords: print("params.all_peds_lr_sorted_by_x: ", params.all_peds_lr_sorted_by_x, "\n")
        if "debug" in params.log_keywords: 
            for ped_i in params.all_peds_lr_sorted_by_x:
                print(ped_i.x, ped_i.y)
        params.all_peds_rl_sorted_by_x = sorted(params.all_peds_rl, key=operator.attrgetter('x'))
        if "debug" in params.log_keywords: print("params.all_peds_rl_sorted_by_x: ", params.all_peds_rl_sorted_by_x, "\n")
        if "debug" in params.log_keywords: 
            for ped_i in params.all_peds_rl_sorted_by_x:
                print(ped_i.x, ped_i.y)

        params.all_peds_ordered = list()
        for ped_i in params.all_peds_lr_sorted_by_x:
            params.all_peds_ordered.append(ped_i)
            params.all_peds_ordered.append("placeholder") # add placeholder every one element
        diff = len(params.all_peds_rl_sorted_by_x) - len(params.all_peds_lr_sorted_by_x)
        if len(params.all_peds_rl_sorted_by_x) > len(params.all_peds_lr_sorted_by_x):
            for i in range(diff): # range(negative int) output nothing
                params.all_peds_ordered.append("placeholder") # add placeholder for right to left ped
        if "debug" in params.log_keywords: print("1 len(params.all_peds_ordered): ", len(params.all_peds_ordered))
      

        if len(params.all_peds_rl_sorted_by_x) >= len(params.all_peds_lr_sorted_by_x):
            for i in range(len(params.all_peds_lr_sorted_by_x)):
                params.all_peds_ordered[i*2 + 1] = params.all_peds_rl_sorted_by_x[i] # replace those placeholder    
            for i in range(diff):
                params.all_peds_ordered[len(params.all_peds_lr_sorted_by_x)*2 + i] = params.all_peds_rl_sorted_by_x[len(params.all_peds_lr_sorted_by_x) + i]
        else:
            for i in range(len(params.all_peds_rl_sorted_by_x)):
                params.all_peds_ordered[i*2 + 1] = params.all_peds_rl_sorted_by_x[i] # replace those placeholder  
      
        
        # delete all remaining placeholder
        for ped_i in params.all_peds_ordered: 
            if "debug" in params.log_keywords: print(ped_i)
            if ped_i == "placeholder":
                params.all_peds_ordered.pop( params.all_peds_ordered.index(ped_i) )
        if "debug" in params.log_keywords: print("2 len(params.all_peds_ordered): ", len(params.all_peds_ordered))
        
        if "debug" in params.log_keywords: 
            for ped_i in params.all_peds_ordered:
                print(ped_i.x, ped_i.y)


    @staticmethod
    def cross_street(params):
        #
        # Move
        #
        params.step_counter = 0
        while not Utilities.is_all_peds_finish(params):
            # order
            BackendAPI.order_peds_leftright_inturn(params)
            for ped_i in params.all_peds_ordered:
                ped_i.move_one_step(params)
            params.step_counter += 1
            # print("\nCurrent step: ", params.step_counter)
            if "core" in params.log_keywords: 
                print("\nAfter one move:\n")
                for ped_i in params.all_peds_ordered:
                    print(ped_i.previousx, " --> ", ped_i.x, " ", ped_i.previousy, " --> ", ped_i.y)
            if "plot" in params.log_keywords: Utilities.plot_positions(params, "moving")

    @staticmethod
    def get_ped_needed_time_to_cross(params):
        used_time = params.step_counter *  params.step_time
        if "core" in params.log_keywords: print("\nFinished! Used time is: ", used_time, "\n")
        if "debug" in params.log_keywords: 
            for ped_i in params.all_peds_ordered:
                print(ped_i.x, ped_i.y)
        return used_time


