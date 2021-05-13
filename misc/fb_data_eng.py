t = [1, 2, 5, 5, 8]


# Given an array of integers, we would like to determine whether the array 
# is monotonic (non-decreasing/non-increasing) or not.
def is_monotonic(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False

    return True


import math


# Find the max no from the given set of elements in an array
def find_max(arr):
    max = -1 * math.inf
    for i in arr:
        if i > max:
            max = i

    return max


# Find the minimum absolute difference between the set of elements of an array.
def find_min_abs(arr):
    sorted_arr = sorted(arr)

    min = math.inf 
    for i in range(1, len(arr)):
        diff = sorted_arr[i] - sorted_arr[i-1]
        if diff < min:
            min = diff 

    return min  

# DDL, ERD 
# P, F key; name; type; type parameter
create table xxx (
    id  integer auto_increment,
    xx  type not null,
    xx  type not null,
    primary key (xxx),
    foreign key fk_name (xxx) references table2(col1) 
        on (delete/update) (cascade/set null/no action/set default)
);

# Recursively parse a string for a pattern that can be either 1 or 2 characters long
def parse_string(str, target):
    if len(str) == 0:
        return []

    head1, tail1 = str[0], str[1:]
    head2, tail2 = str[0:2], str[2:]

    if head1 == target:
        return [head1] + parse_string(tail1, target)
    elif head2 == target:
        return [head2] + parse_string(tail2, target)
    else:
        return parse_string(tail1, target)

# Perform a merge-sort with SQL only.
union and order by 

# Query a many to many relationship while not violating the grain of a fact table.
# without causing duplication? 
select *
from table1
where pk in (select distinct fk1 from association_table where fk2 = xxx)

# Given a number and an array find the sum of any 2 numbers 
# in a list is equal to a given number.
def find_num(num, arr):
    hash = set(arr) 
    for i in arr:
        if num - i in hash:
            return [i, num - i]

    return []

# Design an experiment to test whether a feature spurs conversation.
clarify feature and conversation

A/B test 

# How do you rate the popularity of a posted video online?
view_count, 
like_count, 

time_window, location 

accelaration: day over day, week over week, month over month

# Given an IP address as an input string, validate it and return True/False
def validate_ip(str):
    # 0-255.0-255.0-255.0-255
    splited_str = str.split(".")
    if len(splited_str) < 4:
        return False 

    for i in splited_str:
        if not 0 <= int(i) <= 255:
            return False 

    return True

# Count the neighbors of each node in a graph. input graph is a multidimensional list

# Given a list of tuples of movie watched times, find how many unique minutes of the movie did the viewer watch e.g. [(0,15),(10,25)]. The viewer watched 25 minutes of the movie.

def unique_min(l):
# approach 1:
#    global_state
#    0:1 -> 10:2 -> 15:1 -> 25:0  
#    if gs > 0, count the time
# O(n)

    timeline = []
    hash = {} 

    for t in l:
        timeline.append(t[0])
        timeline.append(t[1])
        hash[t[0]] = 1
        hash[t[1]] = -1

    sorted_tl = sorted(timeline)
    total = 0
    status = 0
    for i in range(len(sorted_tl)):
        if i != 0:
            if status > 0 :
                total += sorted_tl[i] - sorted_tl[i-1]

        status += hash[sorted_tl[i]]

    return total

# approach 2:
# make a list of disjointed periods
# O(n^2)


# How do you delete duplicate in a list?
convert to hash then to list again 

# Given a multi-step product feature, write SQL to see how well this feature is doing (loading times, step completion %). 
# Then use Python to constantly update average step time as new values stream in, given that there are too many to store in memory
with user_step_completed as (
    select user_id, max(step_num) as max_step
    from xxx 
    group by user_id
    where event_name = "step_trigger"
)
select avg(max_step / total_num_of_steps) # give up at certain step?
from user_step_completed

def update_realtime_step(in):
    # update average with limited memory
    count = xxx 
    avg = xxx

    avg = (in + count * avg) / (count + 1)
    count += 1

    return avg 


# How do you join two tables with all the information on the left one unchanged?
left join

# What operator will you use if you want to join a table to tables with one left and matched the right one?
join on 


# The ORDER BY command in SQL is automatically set in what format if you didn’t set it? Ascending or Descending?
asc 

# When you want to delete or add a column of a table in a database, what command you will use?
alter table add column / drop column 

# You have a 2-D array of friends like [["A","B"],["A","C"],["B","D"],["B","C"],["R","M"],["S"],["P"]]
# Write a function that creates a dictionary of how many friends each person has. 
# People can have 0 to many friends. However, there won’t be repeat relationships like [A,B] and [B,A] and neither will there be more than 2 people in a relationship

def make_friends(arr):
    hash = {}

    for i in arr:
        if len(i) == 2:
            # 2 people in a relationship

            hash[i[0]] = hash.get(i[0], 0) + 1
            hash[i[1]] = hash.get(i[1], 0) + 1


        elif len(i) == 1:
            # single person
            hash[i[0]] = 0

    return hash 



