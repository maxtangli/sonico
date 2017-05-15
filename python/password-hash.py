from werkzeug.security import generate_password_hash, check_password_hash

password = 'hello nanoha.'

# salt = method != 'plain' and gen_salt(salt_length) or ''
# h, actual_method = _hash_internal(method, salt, password)
# return '%s$%s$%s' % (actual_method, salt, h)
# pbkdf2:sha256:50000$o9z1T5Te$47428184ecfed48b687441b48923abac0db671d260ff8aa7d9fbcaf145f1f2be
hash = generate_password_hash(password)

# if pwhash.count('$') < 2:
#     return False
# method, salt, hashval = pwhash.split('$', 2)
# return safe_str_cmp(_hash_internal(method, salt, password)[0], hashval)
valid = check_password_hash(hash, password)
print(password, hash, valid, sep='\n')

"""
0.8h 
- code reading: beautiful coding style under modern language
"""