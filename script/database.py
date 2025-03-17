#Number database

mass_options = ["gramo",
                "kilogramo",
                "tonelada",
                "onza",
                "libra",]
distance_options = ["metro",
                    "centimetro",
                    "kilometro",
                    "milimetro",
                    "milla",
                    "pulgada",
                    "pie",
                    "yarda",]
time_options = ["segundo",
                "dia",
                "minuto",
                "hora",]
temperature_options = ["celsius",
                        "fahrenheit",
                        "kelvin",
                        "rankine"]
speed_options = ["metro/segundo",
                "kilometro/hora",
                "milla/hora",
                "nudo",]
pressure_options = ["pascal",
                    "atmosfera",
                    "bar",
                    "mmHg",
                    "psi",]
volume_options = ["litro",
                "centimetros cubicos",
                "metros cubicos",
                "galon",
                "taza",
                "cucharada",
                "cucharadita",]
acceleration_options = [
                        "metro/segundo^2",
                        "g"]
density_options = ["kilogramo/metro^3",
                "gramo/centimetro^3",
                "libra/pie^3"]
energy_options = ["joule",
                "caloria",
                "electron-volt",
                "kilowatt-hora"]
flow_options = ["centimetro^3/segundo",
                "metro^3/hora",
                "litro/segundo",]
area_options = ["metro^2",
                "kilometro^2",
                "milla^2",
                "hectarea"]

options = [mass_options,
           distance_options,
           time_options,
           temperature_options,
           speed_options,
           pressure_options,
           volume_options,
           acceleration_options,
           density_options,
           energy_options,
           flow_options,
           area_options]

mass = {
    "gramo" : 1,
    "kilogramo" : 1000,
    "tonelada" : 1000000,
    "onza" : 28.34952,
    "libra" : 453.5924
}

distance = {
    "metro" : 1,
    "centimetro" : 0.01,
    "kilometro" : 1000,
    "milimetro" : 0.001,
    "milla" : 1609.344,
    "pie" : 0.3048,
    "pulgada" : 0.0254,
    "yarda" : 0.9144,
}

time = {
    "segundo" : 1,
    "dia" : 86400,
    "minuto" : 60,
    "hora" : 3600,
}   

temperature = {
    #En celsius
    #es distinto
}

speed = {
    "metro/segundo" : 1,
    "kilometro/hora" : 0.2777778,
    "milla/hora" : 0.44704,
    "nudo" : 0.5144444
}

pressure = {
    "pascal" : 1,
    "atmosfera" : 101325,
    "bar" : 100000,
    "mmHg" : 133.3224,
    "psi" : 6894.757
}

volume = {
    "litro" : 1,
    "centimetros cubicos" : 0.001,
    "metros cubicos" : 1000,
    "galon" : 3.785412,
    "taza" : 0.2365882,
    "cucharada" : 0.01478676,
    "cucharadita" : 0.004928922,
}

acceleration = {
    "metro/segundo^2" : 1,
    "g" : 9.80665 
}

density = {
    "kilogramo/metro^3" : 1,
    "gramo/centimetro^3" : 1000,
    "libra/pie^3" : 16.01846,
}

energy = {
    "joule" : 1,
    "caloria" : 4.1868,
    "electron-volt" : 0.00000000000000000016021,
    "kilowatt-hora" :  3600000,
}

flow = {
    "centimetro^3/segundo" : 1,
    "metro^3/hora" : 277.7778,
    "litro/segundo" : 1000 
}

area = {
    "metro^2" : 1,
    "kilometro^2" : 1000000,
    "milla^2" : 2589988,
    "hectarea" : 10000,

}

conversion_factors = [
    mass,
    distance,
    time,
    temperature,
    speed,
    pressure,
    volume,
    acceleration,
    density,
    energy,
    flow,
    area,
]

unit_historial = [0]
