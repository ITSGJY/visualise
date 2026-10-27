#!/usr/bin/env python3
from pathlib import Path
import re,sys,xml.etree.ElementTree as ET
def check(path):
 source=path.read_text(encoding="utf-8")
 errors=[]
 if path.suffix==".svg":
  try:
   root=ET.fromstring(source)
   if not root.attrib.get("viewBox"):errors.append("SVG missing viewBox")
  except ET.ParseError as exc:errors.append(str(exc))
 elif path.suffix==".html":
  if "<!doctype html>" not in source.lower():errors.append("missing doctype")
  if 'name="viewport"' not in source:errors.append("missing responsive viewport")
  ids=re.findall(r'\bid=["\x27]([^"\x27]+)["\x27]',source)
  if len(ids)!=len(set(ids)):errors.append("duplicate DOM IDs")
 else:errors.append("unsupported extension")
 for e in errors: print("FAIL",path,e)
 if not errors:print("PASS",path)
 return len(errors)
if __name__=="__main__":
 if len(sys.argv)<2:raise SystemExit("usage: lint_visual.py file.html [file.svg...]")
 raise SystemExit(min(1,sum(check(Path(arg)) for arg in sys.argv[1:])))
