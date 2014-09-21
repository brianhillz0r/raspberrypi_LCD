import urllib2
import json

f = urllib2.urlopen('http://api.wunderground.com/api/69e962e1a8ee7b82/geolookup/conditions/q/MI/Detroit.json')
json_string = f.read()
parsed_json = json.loads(json_string)
loc_city = parsed_json['location']['city']
loc_state = parsed_json['location']['state']
temp_f = parsed_json['current_observation']['temp_f']
message = '{city}, {state}\n{temp} F'.format(city = loc_city, state = loc_state, temp = temp_f)

print loc_city
print loc_state
print temp_f
print message
