# -*- coding: utf-8 -*-
"""Coursework.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zGxRFntpKNPI3tFsBP2SfYCQFwWHre6z

**First task**
"""

import random
import math
import matplotlib.pyplot as plt


_lambda = int(input("Intensity: "))
time_units = int(input("Number of time units: "))

_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0
t = 0
i = 1

print('Index of event' + '  |      ' + 'Time interval' + '      |   ' + 'Absolute event time')

while t < time_units:
  n = random.random()
  _inter_event_time = -math.log(1.0 - n) / _lambda
  t = t + _inter_event_time
  if t > time_units:
    break
  else:
    _event_num.append(i)
    _inter_event_times.append(_inter_event_time)
    _event_time = _event_time + _inter_event_time
    _event_times.append(_event_time)
    print('      ' + str(i)[:10] +'               ' + str(_inter_event_time)[:10] + '               ' + str(_event_time)[:10])
    i = i + 1

y = [0] + _event_num
x = _event_times + [time_units]

fig = plt.figure(figsize=(20,10))
plt.step(x, y)
plt.suptitle('Time')
plt.xlabel('Actual time')
plt.ylabel('Index of event')
plt.plot(x, y, color='red', marker='o', markersize=2, linewidth=0)

_interval_nums = []
_num_events_in_interval = []
_interval_num = 1
_num_events = 0

print('Interval index  |   Number of events in interval')

for i in range(len(_event_times)):
	_event_time = _event_times[i]
	if _event_time <= _interval_num:
		_num_events += 1
	else:
		_interval_nums.append(_interval_num)
		_num_events_in_interval.append(_num_events)
		print('        ' + str(_interval_num) +'                         ' + str(_num_events))
		_interval_num += 1
		_num_events = 1

fig = plt.figure()
fig.suptitle('Number of events occurring in consecutive interval')
plt.bar(_interval_nums, _num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()

"""**Second task**"""

import random
import math
import matplotlib.pyplot as plt
from random import randint

_lambda = 5
i = 1
t = 0
_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0
fans_quantity = []

print('Number of event' + '   |   ' + 'Time diff between consecutive events' + '   |   ' + 'Absolute event time' + '   |   ' + 'Quantity of fans')

while t < 1:
  n = random.random()
  _inter_event_time = -math.log(1.0 - n) / _lambda
  t = t + _inter_event_time
  if t > 1:
    break
  else:
    _event_num.append(i)
    fans = randint(20, 40)
    fans_quantity.append(fans)
    _inter_event_times.append(_inter_event_time)
    _event_time = _event_time + _inter_event_time
    _event_times.append(_event_time)
    print('      ' + str(i)[:10] +'                       ' + str(_inter_event_time)[:10] + '                             ' + str(_event_time)[:10] + '                 ' + str(fans))
    i = i + 1

y = [0] + _event_num
x = _event_times + [1]

fig = plt.figure(figsize=(20,10))
plt.step(x, y)
plt.suptitle('Time')
plt.xlabel('Actual time')
plt.ylabel('Index of event')
plt.plot(x, y, color='red', marker='o', markersize=2, linewidth=0)

fig = plt.figure()
fig.suptitle('Quantity of fans in consecutive buss')
plt.bar(_event_num, fans_quantity)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()

print('Total quantity of fans: ', sum(fans_quantity))

"""**Third task**"""

import random
import math
import matplotlib.pyplot as plt

_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0
i = 1

_lambda = 7
time_units = 10

print('Number of event' + '   |   ' + 'Time diff between consecutive events' + '   |   ' + 'Absolute event time')

while _event_time < time_units:
  n = random.random()
  _inter_event_time = -math.log(1.0 - n) / _lambda
  _event_time = _event_time + _inter_event_time
  if _event_time > time_units:
    break
  else:
    u = random.random()
    func = 3 + (4/(_event_time + 1))
    if u <= func:
      _event_num.append(i)
      _inter_event_times.append(_inter_event_time)
      _event_times.append(_event_time)
      print('      ' + str(i)[:10] +'                       ' + str(_inter_event_time)[:10] + '                          ' + str(_event_time)[:10])
      i = i + 1

y = [0] + _event_num
x = _event_times + [time_units]

fig = plt.figure(figsize=(20,10))
plt.step(x, y)
plt.suptitle('Time')
plt.xlabel('Actual time')
plt.ylabel('Index of event')
plt.plot(x, y, color='red', marker='o', markersize=2, linewidth=0)

_interval_nums = []
_num_events_in_interval = []
_interval_num = 1
_num_events = 0

print('Interval number  |   Number of events in interval')

for i in range(len(_event_times)):
	_event_time = _event_times[i]
	if _event_time <= _interval_num:
		_num_events += 1
	else:
		_interval_nums.append(_interval_num)
		_num_events_in_interval.append(_num_events)
		print('        ' + str(_interval_num) +'                         ' + str(_num_events))
		_interval_num += 1
		_num_events = 1

fig = plt.figure()
fig.suptitle('Number of events occurring in consecutive intervals')
plt.bar(_interval_nums, _num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')

plt.show()

"""**Fourth task**"""

import random
import math
import matplotlib.pyplot as plt

_event_num = []
_inter_event_times = []
_event_times = []
_event_time = 0
_total_time_interval = 0
time_units = 10
i = 1
_lambda = 1
current = 5

print('Number of event' + '      |      ' + 'Time interval' + '      |      ' + 'Absolute event time')

while _event_time < time_units:
  n = random.random()
  _inter_event_time = -math.log(1.0 - n) / _lambda
  if _event_time + _inter_event_time > current:
    _inter_event_time = (_inter_event_time + _event_time - current ) * (_lambda/(_lambda + 5))
    current += 1
    if current == 11:
      break
    _lambda += 5
  _event_time = _event_time + _inter_event_time
  _total_time_interval = _total_time_interval + _inter_event_time 
  n = random.random()
  if current == 5:
    if n <= (_event_time/5)/_lambda:
      _event_num.append(i + 1)
      _inter_event_times.append(_total_time_interval)
      _event_times.append(_event_time)
      print('      ' + str(i) +'                       ' + str(_total_time_interval)[:10] + '               ' + str(_event_time)[:10])
      i += 1
      _total_time_interval = 0
  elif current > 5:
    if n <= (1 + 5*(_event_time - 5))/_lambda:
      _event_num.append(i + 1)
      _inter_event_times.append(_inter_event_time)
      _event_times.append(_event_time)
      print('      ' + str(i) +'                       ' + str(_total_time_interval)[:10] + '               ' + str(_event_time)[:10])
      i += 1
      _total_time_interval = 0

y = [0] + _event_num
x = _event_times + [time_units]

fig = plt.figure(figsize=(30,15))
plt.step(x, y)
plt.suptitle('Time')
plt.xlabel('Actual time')
plt.ylabel('Index of event')
plt.plot(x, y, color='red', marker='o', markersize=2, linewidth=0)

_interval_nums = []
_num_events_in_interval = []
_interval_num = 1
_num_events = 0

print('Interval number  |   Number of events in interval')

for i in range(len(_event_times)):
	_event_time = _event_times[i]
	if _event_time <= _interval_num:
		_num_events += 1
	else:
		_interval_nums.append(_interval_num)
		_num_events_in_interval.append(_num_events)
		print('        ' + str(_interval_num) +'                         ' + str(_num_events))
		_interval_num += 1
		_num_events = 1

fig = plt.figure()
fig.suptitle('Number of events occurring in consecutive intervals')
plt.bar(_interval_nums, _num_events_in_interval)
plt.xlabel('Index of interval')
plt.ylabel('Number of events')
plt.show()