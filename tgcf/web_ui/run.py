import os
from importlib import resources

import tgcf as tg
from tgcf.config import CONFIG

package_dir = resources.path(package=tg, resource="").__enter__()
package_dir = str(package_dir) + "/web_ui"

def main():
    print(package_dir)
    path = os.path.join(package_dir, "0_👋_Hello.py")
    os.environ["STREAMLIT_THEME_BASE"] = CONFIG.theme
    os.environ["STREAMLIT_BROWSER_GATHER_USAGE_STATS"] = "false"
    os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
    os.system(f"streamlit run {path}")
