from statistics import mean, median, variance
from collections import Counter
import sys
from line_protocol_parser import parse_line

class Line:
    def __init__(self, telegraf_metric):
        # parsed_metric is a parsed Telegraf Metric
        _parsed = parse_line(telegraf_metric)
        self.measurement = _parsed["measurement"]
        self.tags = [(k,v) for k,v in _parsed["tags"].items()]
        self.fields = [(k,v) for k,v in _parsed["fields"].items()]
        self.tag_keys = [k for k in _parsed["tags"].keys()]
        self.tag_values = [v for v in _parsed["tags"].values()]
        self.field_keys = [k for k in _parsed["fields"].keys()]
        self.field_values = [v for v in _parsed["fields"].values()]
        self.timestamp = _parsed["time"]
        self.tag_key_lengths = [len(k) for k in self.tag_keys]
        self.tag_value_lengths = [len(v) for v in self.tag_values]
        self.field_key_lengths = [len(k) for k in self.field_keys]
        self.field_value_lengths = [len(v) for v in self.field_values]
        self.int_values = self._parse_value_types(self.fields, int)
        self.float_values = self._parse_value_types(self.fields, float)
        self.bool_values = self._parse_value_types(self.fields, bool)
        self.str_values = self.parse_value_types(self.fields, str)
            

    def _parse_value_types(di: dict, field_type: type):
        return [v for v in di.values() if isinstance(v, field_type)]


def elem_lengths(di: dict, key=False):
    if key:
        return [len(f[0]) for f in di]
    else:
        return [len(f[1]) for f in di]

for telegraf_metric in sys.stdin:
    telegraf_metric   = telegraf_metric.rstrip('\n')
    line              = Line(telegraf_metric)
    measurement       = line.measurement
    num_tags          = len(line.tags)
    tag_key_avg_len   = mean(line.tag_key_lengths)
    tag_val_avg_len   = mean(line.tag_value_lengths)
    field_key_avg_len = mean(elem_lengths(line.fields, key=True))
    int_val_avg_len   = mean(elem_lengths(line.int_values))
    float_val_avg_len = mean(elem_lengths(line.float_values))
    bool_val_avg_len  = mean(elem_lengths(line.bool_values))
    str_val_avg_len   = mean(elem_lengths(line.str_values))

    tag_list          = [f"{k}={v}" for k,v in line.tags]
    tagset_string     = "".join(tag_list)

    # f-string requres Python3 -- will make backwards compatible at a later date
    new_line          = (f"""sizing,measurement={measurement},{tagset_string} num_tags={num_tags},tag_key_avg_len={tag_key_avg_len},
                            tag_val_avg_len={tag_val_avg_len},field_key_avg_len={field_key_avg_len},int_val_avg_len={int_val_avg_len},
                            float_val_avg_len={float_val_avg_len},bool_val_avg_len={bool_val_avg_len},str_val_avg_len={str_val_avg_len} {line.timestamp}""")

    print(new_line)
    sys.stdout.flush()


