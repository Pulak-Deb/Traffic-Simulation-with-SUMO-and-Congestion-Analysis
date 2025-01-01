import traci
import random
import csv

# Start SUMO simulation
traci.start(["sumo-gui", "-c", "mogbazar.sumocfg"])  # Use sumo-gui for visualization

# Base Traffic Flow Data (vehicles per hour)
base_north_south_flow = 3129
base_south_north_flow = 3461
base_east_to_main_flow = 800    # From side roads to main roads
base_main_to_east_flow = 700  # From main roads to side roads
base_west_to_main_flow = 900    # From side roads to main roads
base_main_to_west_flow = 600  # From main roads to side roads

# Vehicle proportions and PCU values
vehicle_types = {
    "passenger_car": {"pcu": 1, "proportion": 0.154},
    "bus": {"pcu": 3, "proportion": 0.0038},
    "motorbike": {"pcu": 0.1, "proportion": 0.3244},
    "cng": {"pcu": 0.5, "proportion": 0.2435},
    "nmv": {"pcu": 0.5, "proportion": 0.2391},
}

# Initialize metrics data
flow_data = []
congestion_data = []

# Open CSV files for writing
with open("flow_data.csv", "w", newline="") as flow_file, \
     open("congestion_data.csv", "w", newline="") as congestion_file:

    flow_writer = csv.writer(flow_file)
    congestion_writer = csv.writer(congestion_file)

    # Write headers to CSV files
    flow_writer.writerow(["Step", "Flow"])
    congestion_writer.writerow(["Step", "Congestion"])

    # Define routes with valid connections
    north_south_route = ["north_in", "ns1", "ns2", "ns3", "ns4", "south_out"]
    south_north_route = ["south_in", "sn1", "sn2", "sn3", "sn4", "sn5", "north_out"]

    main_to_east1_route = ["north_in", "main_to_east1"]
    main_to_east2_route = ["north_in", "ns1", "ns2", "main_to_east2"]
    main_to_east3_route = ["north_in", "ns1", "ns2", "ns3", "main_to_east3"]
    main_to_east4_route = ["north_in", "ns1", "ns2", "ns3", "ns4", "main_to_east4"]

    east_to_main1_route = ["east_to_main1", "ns1", "ns2", "ns3", "ns4", "south_out"]
    east_to_main2_route = ["east_to_main2", "ns3", "ns4", "south_out"]
    east_to_main3_route = ["east_to_main3", "ns4", "south_out"]
    east_to_main4_route = ["east_to_main4", "south_out"]

    main_to_west4_route = ["south_in", "main_to_west4"]
    main_to_west3_route = ["south_in", "sn1", "main_to_west3"]
    main_to_west2_route = ["south_in", "sn1", "sn2", "main_to_west2"]
    main_to_west1_route = ["south_in", "sn1", "sn2", "sn3", "sn4", "sn5", "main_to_west1"]

    west_to_main4_route = ["west_to_main4", "sn1", "sn2", "sn3", "sn4", "sn5", "north_out"]
    west_to_main3_route = ["west_to_main3", "sn2", "sn3", "sn4", "sn5", "north_out"]
    west_to_main2_route = ["west_to_main2", "sn3", "sn4", "sn5", "north_out"]
    west_to_main1_route = ["west_to_main1", "north_out"]

    # Simulation parameters
    simulation_duration = 3600  # 1 hour
    vehicle_counter = 0  # Counter for unique vehicle IDs

    # Generate traffic dynamically
    for step in range(simulation_duration):
        # Time-based variation in traffic flow
        if step < 1200:  # Morning peak (first 20 minutes)
            north_south_flow = base_north_south_flow * 2
            south_north_flow = base_south_north_flow * 2
            east_to_main_flow = base_east_to_main_flow * 1.5
            main_to_east_flow = base_main_to_east_flow * 1.5
            west_to_main_flow = base_west_to_main_flow * 1.5
            main_to_west_flow = base_main_to_west_flow * 1.5
        elif step < 2400:  # Midday (next 20 minutes)
            north_south_flow = base_north_south_flow * 1.5
            south_north_flow = base_south_north_flow * 1.2
            east_to_main_flow = base_east_to_main_flow * 1.2
            main_to_east_flow = base_main_to_east_flow * 1.2
            west_to_main_flow = base_west_to_main_flow * 1.2
            main_to_west_flow = base_main_to_west_flow * 1.2
        else:  # Evening peak (last 20 minutes)
            north_south_flow = base_north_south_flow * 2.5
            south_north_flow = base_south_north_flow * 2
            east_to_main_flow = base_east_to_main_flow * 2
            main_to_east_flow = base_main_to_east_flow * 2
            west_to_main_flow = base_west_to_main_flow * 2
            main_to_west_flow = base_main_to_west_flow * 2

        # Calculate generation rates per second for all directions
        generation_rate = {
            "north_south": north_south_flow / 3600,
            "south_north": south_north_flow / 3600,
            "east_to_main": east_to_main_flow / 3600,
            "main_to_east": main_to_east_flow / 3600,
            "west_to_main": west_to_main_flow / 3600,
            "main_to_west": main_to_west_flow / 3600,
        }

        for direction, rate in generation_rate.items():
            if random.uniform(0, 1) < rate:  # Vehicle generation probability
                vehicle_type = random.choices(
                    list(vehicle_types.keys()),
                    weights=[v["proportion"] for v in vehicle_types.values()]
                )[0]

                # Assign route based on direction
                if direction == "north_south":
                    route = north_south_route
                elif direction == "south_north":
                    route = south_north_route
                elif direction == "east_to_main":
                    route = random.choice([east_to_main1_route, east_to_main2_route, east_to_main3_route, east_to_main4_route])
                elif direction == "main_to_east":
                    route = random.choice([main_to_east1_route, main_to_east2_route, main_to_east3_route, main_to_east4_route])
                elif direction == "west_to_main":
                    route = random.choice([west_to_main1_route, west_to_main2_route, west_to_main3_route, west_to_main4_route])
                elif direction == "main_to_west":
                    route = random.choice([main_to_west1_route, main_to_west2_route, main_to_west3_route, main_to_west4_route])

                route_id = f"{direction}_{vehicle_type}_{step}"
                traci.route.add(route_id, route)

                vehID = f"{vehicle_type}_{vehicle_counter}"
                vehicle_counter += 1

                # Add vehicle
                traci.vehicle.add(
                    vehID=vehID,
                    routeID=route_id,
                    typeID=vehicle_type,
                    depart=str(step)
                )

        # Collect metrics from detectors
        try:
            # Traffic Flow
            flow = traci.inductionloop.getLastStepVehicleNumber("flow_detector_lane1")
            flow_writer.writerow([step, flow])
            flow_data.append(flow)

            # Congestion (Lane Occupancy)
            congestion = traci.lanearea.getLastStepOccupancy("congestion_detector_lane1")
            congestion_writer.writerow([step, congestion])
            congestion_data.append(congestion)

        except Exception as e:
            print(f"Error collecting data at step {step}: {e}")

        traci.simulationStep()

    # Output results to console
    print("Flow Data:", flow_data)
    print("Congestion Data:", congestion_data)

# Close simulation
traci.close()
