# Primer grupo (los que quieres comprobar)
grupo1 = [
    "job458067", "job350247", "job454250", "job370045", "job315202", "job268722", "job137091", "job448341",
    "job116478", "job218879", "job344486", "job216629", "job222547", "job156540", "job168500", "job177358",
    "job327160", "job448150", "job437317", "job373445", "job215652", "job196209", "job440163", "job222822",
    "job256317", "job404759", "job7531", "job239256", "job198997", "job211085", "job112757", "job216225",
    "job4955", "job211117", "job312623", "job217664", "job403210", "job115483", "job116069", "job311303",
    "job323137", "job216627", "job321749", "job200255", "job185363", "job354590", "job411832", "job385166",
    "job202811", "job6200", "job170208", "job111186", "job1053", "job109951", "job429699", "job431998",
    "job290430", "job7419", "job418503", "job5127", "job148660", "job307550", "job110972", "job403640",
    "job112113", "job303830", "job417645", "job377914", "job343132", "job458741", "job441660", "job367570",
    "job400319", "job405752", "job468520", "job364031", "job277865", "job299258", "job318268", "job339914",
    "job175597", "job164386", "job154867", "job283363", "job6144", "job110448", "job266055", "job349311",
    "job306690", "job114279", "job428916", "job134234", "job374340", "job271096", "job219902", "job284461",
    "job144306", "job465161", "job110281", "job328950", "job150962", "job434438", "job208891", "job327962",
    "job161689", "job466411", "job430952", "job270727", "job458629", "job114940", "job416455", "job320376",
    "job205194", "job108094", "job324418", "job1479", "job348717", "job373110", "job311723"
]

# Segundo grupo (los que deben contenerlos todos)
grupo2 = [
    "job1053", "job108094", "job109492", "job109951", "job110281", "job110448", "job110972", "job111186",
    "job112113", "job112757", "job114279", "job114940", "job115483", "job116069", "job116478", "job134234",
    "job137091", "job140730", "job144306", "job1479", "job148660", "job150962", "job154867", "job156540",
    "job161689", "job164386", "job168500", "job170208", "job175597", "job177358", "job185363", "job185911",
    "job196209", "job196475", "job198997", "job200255", "job202811", "job205194", "job208891", "job211085",
    "job211117", "job215652", "job216225", "job216627", "job216629", "job217664", "job218879", "job219902",
    "job222547", "job222822", "job225744", "job226538", "job232619", "job239256", "job256317", "job257831",
    "job266055", "job268722", "job270727", "job271096", "job277865", "job279350", "job281031", "job281745",
    "job283363", "job284461", "job290430", "job297859", "job297975", "job299258", "job303830", "job306690",
    "job307550", "job311303", "job311723", "job312623", "job315202", "job318268", "job320376", "job321749",
    "job323137", "job324418", "job327160", "job327962", "job328950", "job339914", "job343132", "job344486",
    "job348717", "job349311", "job350247", "job354590", "job364031", "job367570", "job370045", "job373110",
    "job373445", "job374340", "job377914", "job385166", "job400319", "job403210", "job403640", "job404759",
    "job405752", "job411832", "job416455", "job417645", "job418503", "job422721", "job428916", "job429699",
    "job430952", "job431998", "job434438", "job437317", "job440163", "job441660", "job448150", "job448341",
    "job454250", "job458067", "job458629", "job458741", "job465161", "job466411", "job468520", "job4955",
    "job5127", "job6144", "job6200", "job7419", "job7531"
]

# Comprobar si están todos
faltan = [job for job in grupo2 if job not in grupo1]

if not faltan:
    print("✅ Todos los job numbers del primer grupo están en el segundo grupo.")
else:
    print("❌ Faltan estos job numbers:")
    for job in faltan:
        print(job)