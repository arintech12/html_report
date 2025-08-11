#!/usr/bin/env python3
import datetime
from pathlib import Path

def generate_report():
    # Read template
    template = Path('report/template.html').read_text()
    
    # Generate report content
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_results = [
        {"name": "Test 1", "status": "Passed", "duration": "1.23s"},
        {"name": "Test 2", "status": "Failed", "duration": "2.45s"},
        {"name": "Test 3", "status": "Passed", "duration": "0.87s"},
    ]
    
    # Format results into HTML
    results_html = ""
    for result in test_results:
        row_class = "success" if result["status"] == "Passed" else "danger"
        results_html += f"""
        <tr class="{row_class}">
            <td>{result['name']}</td>
            <td>{result['status']}</td>
            <td>{result['duration']}</td>
        </tr>
        """
    
    # Insert dynamic content into template
    html = template.replace("{{ timestamp }}", timestamp)
    html = html.replace("{{ results }}", results_html)
    
    # Write to index.html
    Path('index.html').write_text(html)
    print("Report generated successfully!")

if __name__ == "__main__":
    generate_report()
