import hashlib

indexes = [4, 5, 3, 6, 2, 7, 1, 8]

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = ""
key_part_static2_trial = "}"

username_trial = b"FRASER"
key = hashlib.sha256(username_trial).hexdigest()
i = 0
for c in indexes:
    key_part_dynamic1_trial += key[c]
    i += 1
    
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
print(key_full_template_trial)