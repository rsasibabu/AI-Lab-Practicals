facts = {"raining"}
print("Initial facts:", facts)
rules = {
    "raining": "road_wet",
    "road_wet": "drive_carefully",
    "drive_carefully": "reduce_speed"
}
changed = True
while changed:
    changed = False
    for condition, conclusion in rules.items():
        if condition in facts and conclusion not in facts:
            facts.add(conclusion)
            changed = True

print("Facts after interface:")
for fact in facts:
    print(fact)
