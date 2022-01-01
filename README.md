# PyKatsuyou

A Japanese verb/adjective inflections tool for python.  

PyKatsuyou uses these great packages:

- [igo-python](https://github.com/hideaki-t/igo-python) (detecting verbs and adjectives)
- [jaconv](https://github.com/ikegami-yukino/jaconv) (convert katakana --> hiragana)
- [tabulate](https://github.com/astanin/python-tabulate) (print a table)

## Install

```bash
pip install pykatsuyou
```

## Usage

This tool requires that you input the dictionary form of the verb/adjective. Using only hiragana may have strange results (unless it's an irregular verb).

```python
from tabulate import tabulate
from pykatsuyou import getInflections

data = getInflections('する', jsonIndent=2)
print(data['json'])
print(data['list'])

table = getInflections('行く', dataframe=True)
print(tabulate(table, headers='keys', tablefmt='pretty'))
```

### CLI

```bash
pykatsuyou する

pykatsuyou -h

Usage:
pykatsuyou [verb/adjective] [-h/-j/-l]
*Must use dictionary form

Options:
***A table is printed by default***
-h (--help) = outputs this text
-j (--json) = prints json
-l (--list) = prints a list
```

## Output - 行く

### Object

```python
{
    # json contains a json string
	'json': '{
		"Affirmative": {
			"Dict-Form": "行く",
			"Non-Past Polite": "行きます",
			"Past": "行った",
			"Past Polite": "行きました",
			"Te-Form": "行って",
			"Imperative": "行け",
			"Conditional": "行けば",
			"Volitional": "行こう"
		},
		"Negative": {
			"Dict-Form": "行かない",
			"Non-Past Polite": "行きません",
			"Past": "行かなかった",
			"Past Polite": "行きませんでした",
			"Te-Form": "行かなくて",
			"Imperative": "行くな",
			"Conditional": "行かなければ",
			"Volitional": "ｘ"
		}
	}',
	'list': [
		'行きます',
		'行った',
		'行きました',
		'行って',
		'行け',
		'行けば',
		'行こう',
		'行きません',
		'行かなかった',
		'行きませんでした',
		'行かなくて',
		'行くな',
		'行かなければ'
	]
}
```



### Table

<table>
<thead>
<tr><th>Godan Verb     </th><th>Affirmative  </th><th>Negative        </th></tr>
</thead>
<tbody>
<tr><td>Dict-Form      </td><td>行く         </td><td>行かない        </td></tr>
<tr><td>Non-Past Polite</td><td>行きます     </td><td>行きません      </td></tr>
<tr><td>Past           </td><td>行った       </td><td>行かなかった    </td></tr>
<tr><td>Past Polite    </td><td>行きました   </td><td>行きませんでした</td></tr>
<tr><td>Te-Form        </td><td>行って       </td><td>行かなくて      </td></tr>
<tr><td>Imperative     </td><td>行け         </td><td>行くな          </td></tr>
<tr><td>Conditional    </td><td>行けば       </td><td>行かなければ    </td></tr>
<tr><td>Volitional     </td><td>行こう       </td><td>ｘ              </td></tr>
</tbody>
</table>
