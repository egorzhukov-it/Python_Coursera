import argparse
import tempfile
import json
import os.path


parser = argparse.ArgumentParser(description='Key Value Storage')
parser.add_argument('--key', help='Input Key')
parser.add_argument('--value', help='Input Value')

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage1.data')
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        json.dump({}, f, ensure_ascii=False)
        f.close()


with open(storage_path, 'r') as f1:
    data_loaded = dict(json.load(f1))
    f1.close()
    if args.key and args.value:
        if args.key not in data_loaded.keys():
            data_loaded[args.key] = [args.value]
        else:
            data_loaded[args.key].append(args.value)
        with open(storage_path, 'w') as f2:
            json.dump(data_loaded, f2, ensure_ascii=False)
            f2.close()
    elif args.key not in data_loaded.keys():
        print(None)
    else:
        print(', '.join(data_loaded[args.key]))





