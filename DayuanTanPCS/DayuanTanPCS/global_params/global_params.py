class global_params:
    def __init__(self):
        super().__init__()

        #
        # log system: Choose any from "core", "debug", "plot" as log keywords, then it will print different levels of logs.
        # For common use, you many want to leave self.log_keywords as empty. 
        # Include "core" to print some basic information. Include "plot" to plot pedestrians position for each step. Include "debug" to print helpful variables values.
        # If include "debug", it is recommended to run like this "python3 backend_example.py > log.txt" since the log would be huge.
        # 
        # self.log_keywords = ["core", "debug", "plot", "debug_100newpos"]
        # self.log_keywords = ["core", "plot"]
        self.log_keywords = ["core"]
        # self.log_keywords = []

        #
        # params needed in both gui and backend
        #

        self.step_time = 1 # seconds; each simulation step reflects how long in read world
        self.step_counter = 0 # how many simulation steps it use
        self.total_needed_time = 0

        # distribution type
        self.distribution_type = 1 # 1 for normal distribution (defult, recommended), 2 for poisson distribution, 3 for T distribution

        # normal distribution conf
        self.sigma_coefficient = 3 #didn't use so far


        # simulation area with default value
        self.crosswalk_width = 300 #cm
        self.crosswalk_length = 1000 #cm
        self.waiting_area_width = self.crosswalk_width
        self.waiting_area_length = 300 #cm
        self.total_length = self.waiting_area_length * 2 + self.crosswalk_length
        self.outside_margin_width = 100 # cm

        self.waiting_area_position_x_offset_min = 0 - self.waiting_area_length
        self.waiting_area_position_x_offset_max = self.waiting_area_length
        self.waiting_area_position_x_offset_mean = 0 #coordinate
        self.waiting_area_position_x_offset_sigma = self.waiting_area_length / 2 # max = mean + 2*sigma

        self.waiting_area_position_y_min = 0
        self.waiting_area_position_y_max = self.crosswalk_width
        self.waiting_area_position_y_mean = self.crosswalk_width / 2 #coordinate
        self.waiting_area_position_y_sigma = self.crosswalk_width / 2 # max = mean + 2*sigma => sigma = (max - mean )/2

        # simulation amount with default value
        self.ped_amount_lr = 10
        self.ped_amount_rl = 10
        self.wheelchair_amount_lr = 1
        self.wheelchair_amount_rl = 1
        self.crutches_user_amount_lr = 1
        self.crutches_user_amount_rl = 1
        self.children_amount_lr = 1
        self.children_amount_rl = 1
        self.elder_amount_lr = 1
        self.elder_amount_rl = 1

        # simulation speed with default value
        self.ped_walking_speed_min = 110 #cm/s
        self.ped_walking_speed_max = 140 #cm/s
        self.ped_walking_speed_mean = 125 #cm/s
        self.ped_walking_speed_sigma = (self.ped_walking_speed_max - self.ped_walking_speed_mean) / 3  # standard deviation # max = mean + 3*sigma => sigma = (max - mean )/3
 
        self.wheelchair_rolling_speed_min = 70 #cm/s
        self.wheelchair_rolling_speed_max = 100 #cm/s
        self.wheelchair_rolling_speed_mean = 85 #cm/s
        self.wheelchair_rolling_speed_sigma = (self.wheelchair_rolling_speed_max - self.wheelchair_rolling_speed_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.crutches_user_walking_speed_min = 50 #cm/s
        self.crutches_user_walking_speed_max = 80 #cm/s
        self.crutches_user_walking_speed_mean = 75 #cm/s
        self.crutches_user_walking_speed_sigma = (self.crutches_user_walking_speed_max - self.crutches_user_walking_speed_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.children_walking_speed_min = 50 #cm/s
        self.children_walking_speed_max = 80 #cm/s
        self.children_walking_speed_mean = 75 #cm/s
        self.children_walking_speed_sigma = (self.children_walking_speed_max - self.children_walking_speed_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        self.elder_walking_speed_min = 50 #cm/s
        self.elder_walking_speed_max = 80 #cm/s
        self.elder_walking_speed_mean = 75 #cm/s
        self.elder_walking_speed_sigma = (self.elder_walking_speed_max - self.elder_walking_speed_mean) / 3 # max = mean + 3*sigma => sigma = (max - mean )/3

        # simulation occupied space with default value
        # Radius is dynamically adjusted using same proportional as speed adjusting.
        # min radius 
        self.radius_of_space_occupied_when_standing = {
            "ped": 30, #cm
            "wheelchair": 70, 
            "crutches_user": 40,
            "child": 30,
            "elder": 30
        }
        # max radius
        self.radius_of_space_occupied_when_moving = {
            "ped": 50, #cm
            "wheelchair": 70, 
            "crutches_user": 90,
            "child": 40,
            "elder": 50
        }

        self.all_peds_lr = list() # all ped who want go from left to right
        self.all_peds_rl = list() # all ped who want go from right to left
        self.all_peds = list()  # all ped 
        self.total_size = 0
        self.all_peds_lr_sorted_by_x = list() # all sorted ped who want go from left to right, sorted by x reversed, biggest x first
        self.all_peds_rl_sorted_by_x = list() # all sorted ped who want go from right to left, sorted by x, smallest x first 
        self.all_peds_ordered = list() # combine above two, like this [ped1_lr, ped1_rl, ped2_lr, ped2_rl, ped3_lr, ped3_rl, ...]

        #
        # params needed only in gui 
        #
        self.global_plot_zoom = 1

        # gui display, left section params input 
        self.crosswalk_width_entry = 0
        self.crosswalk_length_entry = 0
        self.ped_amount_lr_entry = 0
        self.ped_amount_rl_entry = 0
        self.wheelchair_amount_lr_entry = 0
        self.wheelchair_amount_rl_entry = 0
        self.children_amount_lr_entry = 0
        self.children_amount_rl_entry = 0

        # gui display, avd params input 
        self.step_time_entry = 0
        self.waiting_area_length_entry = 0
        self.ped_walking_speed_min_entry = 0
        self.ped_walking_speed_max_entry = 0
        self.ped_walking_speed_mean_entry = 0
        self.wheelchair_rolling_speed_min_entry = 0
        self.wheelchair_rolling_speed_max_entry = 0
        self.wheelchair_rolling_speed_mean_entry = 0
        self.crutches_user_walking_speed_min_entry = 0
        self.crutches_user_walking_speed_max_entry = 0
        self.crutches_user_walking_speed_mean_entry = 0
        self.children_walking_speed_min_entry = 0
        self.children_walking_speed_max_entry = 0
        self.children_walking_speed_mean_entry = 0
        self.elder_walking_speed_min_entry = 0
        self.elder_walking_speed_max_entry = 0
        self.elder_walking_speed_mean_entry = 0
        self.distribution_type_entry = 1
        
        self.frame = 0

        # gui display, second window, ped crossing 
        self.cross_window = 0
        self.cross_frame = 0
        self.cross_frame_width = 1200
        self.cross_frame_height = 600
        self.cross_bg_canvas = 0
        self.background = 0
        self.waiting_area_left_canvas_images_dict = dict()
        self.ped_lr_img = 0
        
