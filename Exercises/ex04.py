name = 'Zed Shaw'
age = 35
height = 74 # inches
weight = 180 # lbs
eye_color = 'blue'
hair_color = 'brown'
metric_inch_conversion_rate = 2.54
metric_lb_conversion_rate = .454
metric_height = height * metric_inch_conversion_rate
metric_weight = weight * metric_lb_conversion_rate

print(f"Let's talk about {name}")
print(f"He's {height} inches tall")
print(f"He's {weight} pounds heavy")
print(f"He's got {eye_color} eyes and {hair_color} hair")

total = age + metric_height + metric_weight
print(f"If I add {age}, {metric_weight}, and {metric_height} I get {total}")
