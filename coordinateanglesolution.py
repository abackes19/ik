# inverse kinematics take 1!
# math syntax: https://docs.python.org/2/library/math.html
import math

d_one = 12 # arbitrary number. this is the distance from shoulder to elbow
d_two = 14 # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

x = 6 # given x input- how we tell robot where to go
y = 7 # given y input- how we tell robot where to go

d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist
sqd_three = math.pow(d_three, 2)
a_three = math.acos((sqd_one + sqd_two - sqd_three) / (2 * sqd_one * sqd_two)) # angle of elbow using law of cosines
a_two = math.asin((d_two * math.sin(a_three)) / d_three) # angle between shoulder and wrist
a_one = 2 * math.pi - (a_three + a_two) # angle between elbow and shoulder
a_four = math.atan(y / x) # angle between 0 line and wrist

a_shoulder = a_four + a_two # angle the shoulder joint should be at from the 0 line
a_elbow = a_three # elbow angle, flush back to shoulder is 0


print a_shoulder

print a_elbow
