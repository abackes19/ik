# inverse kinematics take 1!
# math syntax: https://docs.python.org/2/library/math.html
import math
import fractions
import sys

d_one = 10 # the distance from shoulder to elbow
d_two = 6 # distance from elbow to wrist
sqd_one = math.pow(d_one, 2)
sqd_two = math.pow(d_two, 2)

x = 6 # given x input- how we tell robot where to go
y = 7 # given y input- how we tell robot where to go

# something is wrong

d_three = math.sqrt(math.pow(y, 2) + math.pow(x, 2)) # determining distance from shoulder to wrist ^
o_reach = d_one + d_two
if d_three > o_reach:
    sys.exit("Out of reach: too far away.")
i_reach = d_one - d_two
if d_three < i_reach:
    sys.exit("Out of reach: too close.")
sqd_three = math.pow(y, 2) + math.pow(x, 2)
a_three = math.acos((sqd_one + sqd_two - sqd_three) / (2 * d_one * d_two))
a_two = math.asin((d_two * math.sin(a_three) / d_three)) # angle between shoulder and wrist
a_four = math.atan2(y , x) # angle between 0 line and wrist
print a_two
print a_three
print a_four
print a_four + a_two
a_shoulder = (a_four + a_two) * 180/math.pi # angle the shoulder joint should be at from the 0 line
a_elbow = a_three * 180/math.pi # elbow angle, flush back to shoulder is 0

print "Distance from base: %i units" % d_three
print "Shoulder: %i degrees" % a_shoulder
print "Elbow: %i degrees" % a_elbow
