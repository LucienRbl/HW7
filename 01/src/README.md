
## Transformation of format

### Usage :

```bash
python Parser.py <path/to/txt/file>
```
(if no path is specified the default file is exampleData1.txt)  

**Example** :

```bash
python Parser.py ./my_text.txt > result.json
```

### Result :

The file is transformed from a txt format to a json format. Using the following command :

```bash
python Parser.py ./exampleData2.txt > exampleData2.json
```

```txt
Dear Sir,
I hope this message finds you well.

please find the details about my booking below:

===
Tour id: "4"
Location: "Prague"
Person: "Edgar Snap"
Start Date: "14/10/2025"
End Date: "16/10/2025"
Note: "Peanut allergy"
===

Thank you 

Edgar Snap
```
Became

```json
{
  "id": "4",
  "location": "Prague",
  "person": {
    "name": "Edgar",
    "surname": "Snap"
  },
  "start_date": "14/10/2025",
  "end_date": "16/10/2025",
  "note": "Peanut allergy"
}
```