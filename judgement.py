def start_judgement():
    print "Initiating judgement > "
    ans = True
    while ans:
        print """
                    1. Scenario on a round about exit with 4 exits
                    2. Scenario on a T-point with 3 exits
                    3.Exit
                    """
        ans = raw_input("What would you like to do ? ")
        if ans == "1":
            load_scenario_4()   # make an inline menu
        elif ans == "2":
            load_scenario_3()
        elif ans == "3":
            print "Exiting !"
            exit()
        elif ans != "":
            print "Invalid choice... try again!"


def load_scenario_4():
    print "Scenario for a case with 4 exits : "
    print "REMEMBER , WE HAVE 3 TYPES OF DENSITIES > LOW/MEDIUM/HIGH"
    lane_1_density = raw_input("Enter type of density on lane 1 > ")
    lane_2_density = raw_input("Enter type of density on lane 2 > ")
    lane_3_density = raw_input("Enter type of density on lane 3 > ")
    lane_4_density = raw_input("Enter type of density on lane 4 > ")
    print "Since in a 4 way round about, only one light would be green so, "
    green_for = raw_input("Enter which lane had green light (1,2,3 or 4) >")
    if lane_1_density is "low" and lane_2_density is "low" and lane_3_density is "low" and lane_4_density is "low":
        print "All lanes have low density >"


def load_scenario_3():
    print "Scenario for a case with 3 exits like a T-point > "
    lane_1_density = raw_input("Enter type of density on lane 1 > ")
    lane_2_density = raw_input("Enter type of density on lane 2 > ")
    lane_3_density = raw_input("Enter type of density on lane 3 > ")
    print "Since in a 3 way T-point, more than 1 light can be green, so "
    green_for_0 = raw_input("Enter which lane had green light (1,2 or 3) > ")
    green_for_1 = raw_input("any other lane had green ? (1,2,3 or none) > ")
    if green_for_1 is green_for_0:
        print "Make some sense, you passed same argument on both questions, assuming none for second..."
        green_for_1 = None
    elif green_for_1 is "none":
        print "Okay, so just 1 outgoing line .... "
    else:
        print ":? Something went wrong...."


def cases_for_4():
    print "Standard red light timing(sec) = 60sec "
    red_timer = 60
    green_timer = 20


def master():
    green_time_left = raw_input("time left for green ? ")
    value = 5
    if green_time_left <= value:
        return False
