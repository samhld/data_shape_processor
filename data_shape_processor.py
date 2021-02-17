from statistics import median, variance
import os
from collections import Counter
import re
import numpy as np
import sys
from line_protocol_parser import parse_line

measurements, tags, fields, timestamps = [], [], [], []

class Line:
     def __init__(self, telegraf_metric):
         # parsed_metric is a parsed Telegraf Metric
         _parsed = parse_line(telegraf_metric)
         self.tags = [_parsed["tags"]

for telegraf_metric in sys.stdin:
    telegraf_metric.rstrip('\n')
    line = Line(telegraf_metric)

    
    

    sys.stdout.flush()


def parse_metrics(metric):

    # check with Steven -- does this have access to the `metric` type in Telegraf?
    for i,line in enumerate(metrics.splitlines()):
        if len(re.split('(?<!\\\\)\s', line)) == 3:
            line_tags, line_fields, timestamp = re.split('(?<!\\\\)\s', line)
            line_tags = line_tags.split(',')
            measurement = line_tags.pop(0)
            measurements.append(measurement)
            line_fields = line_fields.split(',')
            tags.extend(line_tags)
            fields.extend(line_fields)
            timestamps.extend(timestamp)

        elif len(re.split('(?<!\\\\)\s', line)) == 2 and no_timestamps == True:
            print(f"This line was disqualified due to formatting issues:\n{line}")
            bad_lines[f'{i}'] = line
            line_tags, line_fields = re.split('(?<!\\\\)\s', line)
            line_tags = line_tags.split(',')
            measurement = line_tags.pop(0)
            measurements.append(measurement)
            line_fields = line_fields.split(',')
            tags.extend(line_tags)
            fields.extend(line_fields)
            
    except ValueError:
        print(f"This line was disqualified due to formatting issues:\n{line}")
    
    else:
        try:
            bad_lines = {}
            for i,line in enumerate(text.splitlines()):
                if len(re.split('(?<!\\\\)\s', line)) == 3:
                    line_tags, line_fields, timestamp = re.split('(?<!\\\\)\s', line)
                    line_tags = line_tags.split(',')
                    measurement = line_tags.pop(0)
                    measurements.append(measurement)
                    line_fields = line_fields.split(',')
                    tags.append(line_tags)
                    fields.append(line_fields)
                    timestamps.append(timestamp)
        except ValueError:
            print(f"This line was disqualified due to formatting issues:\n{line}")

    return (measurements, tags, fields, timestamps)


def intake(metrics, flattened=True):

    num_lines = len(text.splitlines())
    measurements, tags, fields, timestamps = [], [], [], []
    measurements, tags, fields, timestamps = _parse(metrics)
    _tags_dict = { f"Line{i+1} tags": len(elem) for i,elem in enumerate(tags)}
    _fields_dict = { f"Line{i+1} fields": len(elem) for i,elem in enumerate(fields)}
    no_timestamps = no_timestamps
    pattern = re.compile(r'(.*)=(.*)')
    tag_keys, tag_values = _parse_primitives(tags)
    field_keys, field_values = _parse_primitives(fields)
    float_values, int_values, bool_values, str_values = _infer_field_types(field_values)
    if int_values:
        avg_int_value = mean(int_values)
    if float_values:
        avg_float_value = mean(float_values)
    if bool_values:
        avg_bool_value = mean(bool_values)
    if str_values:
        avg_str_value = mean(str_values)
    # if text is str:
    #     num_lines = sum(1 for line in text.splitlines())
    # if text is list:
    #     num_lines = sum(1 for line in text)


def _parse_primitives(self, primitives):
    """Returns tuple of 2 lists of keys and values of either Tags or Fields"""
    pattern = re.compile(r'(.*)=(.*)')
    keys, values = [], []
    for prim in primitives:
        keys.append(pattern.match(prim).group(1))
        values.append(pattern.match(prim).group(2))
    return (keys, values)

def _infer_field_types(self, values):

    fl_pattern = re.compile(r'\d+\.\d+') # distinguish floats from ints with presence of decimal       
    floats, ints, strs, bools = [], [], [], []
    for val in values:
        if val.endswith('i'):
            ints.append(val)
        elif fl_pattern.match(val):
            floats.append(fl_pattern.match(val).string)
        elif val in ('True','true','False','false'):
            bools.append(val)
        else:
            strs.append(val)

    return floats, ints, bools, strs

def line_by_line_schema(self, text):
    schema_dict = dict()
    for i, line in enumerate(text.splitlines()):
        field_values = _parse_primitives(fields)[1]
        schema_dict[f"Line_{i+1}_floats"], schema_dict[f"Line_{i+1}_ints"], schema_dict[f"Line_{i+1}_bools"], schema_dict[f"Line_{i+1}_strs"] = _infer_field_types(field_values)
    return schema_dict

def total_fields(self):
    _total_fields = sum(_fields_dict.values())
    return _total_fields

def total_tags(self):
    _total_tags = sum(_tags_dict.values())
    return _total_tags

def max_tags(self):
    # returns the tag count of the line with the most tags
    _max_tags = max(_tags_dict.values())
    return _max_tags

def max_fields(self):
    # returns the field count of the line with the most fields
    _max_fields = max(_fields_dict.values())
    return _max_fields

def min_tags(self):
    # returns the tag count of the line with the fewest tags
    _min_tags = min(_tags_dict.values())
    return _min_tags

def min_fields(self):
        # returns the field count of the line with the fewest fields
    _min_fields = min(_fields_dict.values())
    return _min_fields       

def mean_fields(self):
    # per line
    return total_fields() / num_lines

def mean_tags(self):
    # per line
    return total_tags() / num_lines

def median_tags(self):
    _median_tags = median(_tags_dict.values())
    return _median_tags

def median_fields(self):
    _median_fields = median(_fields_dict.values())
    return _median_fields

# def mode_tags(self):
#     _mode_tags = Counter(_tags_dict.values()).most_common(1)[0][0]
#     return _mode_tags

# def mode_fields(self):
#     _mode_fields = Counter(_fields_dict.values()).most_common(1)[0][0]
#     return _mode_fields

def mode_tags(self, value='mode'):
    if value == 'mode':
        # mode is the number of tags that occurred most often
        _mode_tags = Counter(_tags_dict.values()).most_common(1)[0][0]
        return _mode_tags
    if value == 'occurrences':
        # number of times the mode occurred
        _mode_tag_occurrences = Counter(_tags_dict.values()).most_common(1)[0][1]
        return _mode_tag_occurrences

def mode_fields(self, value='mode'):
    if value == 'mode':
        # mode is the number of fields that occurred most often
        _mode_fields = Counter(_fields_dict.values()).most_common(1)[0][0]
        return _mode_fields
    if value == 'occurrences':
        # number of times the mode occurred
        _mode_field_occurrences = Counter(_fields_dict.values()).most_common(1)[0][1]
        return _mode_field_occurrences

def distinct_measurements(self):
    _distinct_measurements = len(set(measurements))
    return _distinct_measurements

def tag_variance(self):
    _tag_variance = variance(list(_tags_dict.values()))
    return _tag_variance

def field_variance(self):
    _field_variance = variance(list(_fields_dict.values()))
    return _field_variance

def tag_stddev(self):
    tag_variance()
    _tag_stddev = math.sqrt(_tag_variance)
    return _tag_stddev

def field_stddev(self):
    field_variance()
    _field_stddev = math.sqrt(_field_variance)
    return _field_stddev

def tag_counts(self):
    _tag_counts = Counter(_tags_dict.values())
    return dict(_tag_counts)

def field_counts(self):
    _field_counts = Counter(_fields_dict.values())
    return _field_counts

def tag_bar_plot(self):
    tag_counts()
    _counts_dict = dict(_tag_counts)
    plt.bar(range(len(_counts_dict)), list(_counts_dict.values()))
    plt.xticks(range(len(_counts_dict)), list(_counts_dict.keys()))
    plt.ylabel('Tag Counts')
    plt.title('Count of Occurrences of Tags Per Line')
    plt.show()

def field_bar_plot(self):
    field_counts()
    _counts_dict = dict(_field_counts)
    plt.bar(range(len(_counts_dict)), list(_counts_dict.values()))
    plt.xticks(range(len(_counts_dict)), list(_counts_dict.keys()))
    plt.ylabel('Tag Counts')
    plt.title('Count of Occurrences of Tags Per Line')
    plt.show()

def mean(self, li):
    return sum(map(len, li)) / len(li)
    
def describe(self, t='dict'):
    # 't' is return type-->can be 'dict' or 'dataframe'
    description = {
        'Mean tags per line': mean_tags(),
        'Average fields per line': mean_fields(),
        'Tags mode': mode_tags(),
        'Fields mode': mode_fields(),
        'Tags median': median_tags(),
        'Fields median': median_fields(),
        'Count distinct measurements': distinct_measurements(),
        'Mean Field key': mean(field_keys),
        'Mean Field value': mean(field_values),
        'Mean Tag key': mean(tag_keys),
        'Mean Tag value': mean(tag_values)
        # 'Tag variance': tag_variance(),
        # 'Field variance': field_variance(),
        # 'Tag stddev': tag_stddev(),
        # 'Field stddev': field_stddev()
    }
    if  t == 'dict':
        return description
    elif t  == 'dataframe':
        try:
            import pandas as pd
            return pd.DataFrame(description, np.array([description.keys()]))
        except ModuleNotFoundError:
            print("Please install pandas module to use Dataframes")
