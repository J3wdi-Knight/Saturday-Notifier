from pathlib import Path
from shabbat_cal import Shabbat

def main():
    conf_path = Path('../config/config_data.json').resolve()
    if not conf_path.exists():
        conf_path.parent.mkdir(parents=True, exist_ok=True)
        conf_path.touch()

    return Shabbat().start

if __name__ == '__main__':
    main()
