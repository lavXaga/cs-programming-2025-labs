# Задание 1
a = [("Containment Cell A", 4), ("Archive Vault", 1), ("Bio Lab Sector", 3), ("Observation Wing", 2)]
b = sorted(a, key=lambda x: x[1])
print("Сортировка по уровню угрозы:", b)

# Задание 2
c = [
    {"name": "Dr. Shaw", "shift_cost": 120, "shifts": 15},
    {"name": "Agent Torres", "shift_cost": 90, "shifts": 22},
    {"name": "Researcher Hall", "shift_cost": 150, "shifts": 10}
]
d = list(map(lambda x: x["shift_cost"] * x["shifts"], c))
print("Общая стоимость работы:", d)
e = max(d)
print("Максимальная стоимость:", e)

# Задание 3
f = [
    {"name": "Dr. Klein", "clearance": 2},
    {"name": "Agent Brooks", "clearance": 4},
    {"name": "Technician Reed", "clearance": 1}
]
g = list(map(lambda x: {
    "name": x["name"],
    "clearance": x["clearance"],
    "category": "Restricted" if x["clearance"] == 1 else 
               "Confidential" if 2 <= x["clearance"] <= 3 else 
               "Top Secret"
}, f))
print("Сотрудники с категориями:", g)

# Задание 4
h = [
    {"zone": "Sector-12", "active_from": 8, "active_to": 18},
    {"zone": "Deep Storage", "active_from": 0, "active_to": 24},
    {"zone": "Research Wing", "active_from": 9, "active_to": 17}
]
i = list(filter(lambda x: x["active_from"] >= 8 and x["active_to"] <= 18, h))
print("Дневные зоны:", i)

# Задание 5
reports = [
    {"author": "Dr. Moss", "text": "Analysis completed. Reference: http://external-archive.net"},
    {"author": "Agent Lee", "text": "Incident resolved without escalation."},
    {"author": "Dr. Patel", "text": "Supplementary data available at https://secure-research.org"},
    {"author": "Supervisor Kane", "text": "No anomalies detected during inspection."},
    {"author": "Researcher Bloom", "text": "Extended observations uploaded to http://research-notes.lab"},
    {"author": "Agent Novak", "text": "Perimeter secured. No external interference observed."},
    {"author": "Dr. Hargreeve", "text": "Full containment log stored at https://internal-db.scp"},
    {"author": "Technician Moore", "text": "Routine maintenance completed successfully."},
    {"author": "Dr. Alvarez", "text": "Cross-reference materials: http://crosslink.foundation"},
    {"author": "Security Officer Tan", "text": "Shift completed without incidents."},
    {"author": "Analyst Wright", "text": "Statistical model published at https://analysis-hub.org"},
    {"author": "Dr. Kowalski", "text": "Behavioral deviations documented internally."},
    {"author": "Agent Fischer", "text": "Additional footage archived: http://video-storage.sec"},
    {"author": "Senior Researcher Hall", "text": "All test results verified and approved."},
    {"author": "Operations Lead Grant", "text": "Emergency protocol draft shared via https://ops-share.scp"}
]
j = list(filter(lambda x: "http" in x["text"], reports))
print("Отчеты со ссылками:")
for r in j:
    print(r["author"], "-", r["text"].replace("http", "[ДАННЫЕ УДАЛЕНЫ]").replace("https", "[ДАННЫЕ УДАЛЕНЫ]"))

# Задание 6
k = [
    {"scp": "SCP-096", "class": "Euclid"},
    {"scp": "SCP-173", "class": "Euclid"},
    {"scp": "SCP-055", "class": "Keter"},
    {"scp": "SCP-999", "class": "Safe"},
    {"scp": "SCP-3001", "class": "Keter"}
]
l = list(filter(lambda x: x["class"] != "Safe", k))
print("Объекты с усиленными мерами:", l)

# Задание 7
m = [
    {"id": 101, "staff": 4},
    {"id": 102, "staff": 12},
    {"id": 103, "staff": 7},
    {"id": 104, "staff": 20}
]
n = sorted(m, key=lambda x: x["staff"], reverse=True)[:3]
print("Три самых ресурсоемких инцидента:", n)

# Задание 8
o = [("Lockdown", 5), ("Evacuation", 4), ("Data Wipe", 3), ("Routine Scan", 1)]
p = list(map(lambda x: f"Protocol {x[0]} - Criticality {x[1]}", o))
print("Протоколы:")
for item in p:
    print(item)

# Задание 9
q = [6, 12, 8, 24, 10, 4]
r = list(filter(lambda x: 8 <= x <= 12, q))
print("Смены от 8 до 12 часов:", r)

# Задание 10
s = [
    {"name": "Agent Cole", "score": 78},
    {"name": "Dr. Weiss", "score": 92},
    {"name": "Technician Moore", "score": 61},
    {"name": "Researcher Lin", "score": 88}
]
t = max(s, key=lambda x: x["score"])
print("Лучший результат:", t["name"], "-", t["score"])
