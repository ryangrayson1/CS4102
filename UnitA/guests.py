#missing is d
invs = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
rsvp = ["b", "n", "f", "k", "l", "e", "a", "m", "c", "h", "j", "i", "g"]

#missing is i
invs2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
rsvp2 = ["k", "c", "h", "j", "a", "g", "b", "d", "f", "e"]

def missing_guest(invites, rsvps):
    l = len(invites)

    #base case
    if l == 2:
        if invites[0] != rsvps[0]:
            return invites[0]
        else:
            return invites[1]
    elif l == 1:
        return invites[0]

    #partition guest
    pg = invites[l // 2]

    left = []
    right = []
    #partition the list on pg
    for i in range(len(rsvps)):
        if rsvps[i] < pg:
            left.append(rsvps[i])
        elif rsvps[i] > pg:
            right.append(rsvps[i])

    if len(left) + len(right) == len(rsvps):
        return pg

    elif l % 2 == 1:
        if len(left) < len(right): #this means the missing guest is in the left side of invites
            return missing_guest(invites[:l // 2], left)
        else: #missing guest is in right side of invites
            return missing_guest(invites[l // 2 + 1:], right)

    else:
        if len(left) == len(right):
            return missing_guest(invites[:l // 2], left)
        else: #missing guest is in right side of invites
            return missing_guest(invites[l // 2 + 1:], right)


print(missing_guest(invs, rsvp))
print(missing_guest(invs2, rsvp2))
