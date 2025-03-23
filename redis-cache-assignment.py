import redis

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

# Insert cache entries
r.set('CMPE272', 'Redis Cache Assignment')
r.set('Assignment_StartDate', 'March 06, 2025')
r.set('AssignmentCompletionDate', 'March 23, 2025')
r.set('PurposeOfEducation', 'Help Friends, Family, Society, and Humanity')

# Retrieve values
print("CMPE272:", r.get('CMPE272').decode())
print("Assignment_StartDate:", r.get('Assignment_StartDate').decode())
print("AssignmentCompletionDate:", r.get('AssignmentCompletionDate').decode())
print("PurposeOfEducation:", r.get('PurposeOfEducation').decode())
