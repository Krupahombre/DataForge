require 'json'
require 'vinbot'

if ARGV.length != 2
  exit(1)
end

num_of_vehicles = ARGV[0].to_i

if num_of_vehicles <= 0
  exit(1)
end

file_name = ARGV[1]
vehicles_data = []

num_of_vehicles.times do
  vehicle = Vinbot::Vehicle.new
  vehicle_data = {
    make: vehicle.make,
    model: vehicle.model,
    year: vehicle.year,
    vehicle_type: vehicle.vehicle_type,
    body_type: vehicle.body_type,
    drivetrain: vehicle.drivetrain,
    engine_type: vehicle.engine_type,
    transmission: vehicle.transmission,
    trim: vehicle.trim,
    exterior_colors: vehicle.exterior_colors,
    interior_colors: vehicle.interior_colors,
    vin: vehicle.vin
  }
  vehicles_data << vehicle_data
end

File.open(file_name, 'w') do |file|
  file.write(JSON.pretty_generate(vehicles_data))
end