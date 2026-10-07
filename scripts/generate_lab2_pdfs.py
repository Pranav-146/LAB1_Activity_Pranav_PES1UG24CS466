import base64
import os
from playwright.sync_api import sync_playwright

def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode("utf-8")
        ext = os.path.splitext(image_path)[1].replace(".", "").lower()
        if ext == "jpg":
            ext = "jpeg"
        return f"data:image/{ext};base64,{encoded}"

b64_backlog = get_base64_image("jira_backlog_view.png")
b64_burndown = get_base64_image("jira_burndown_chart_view.png")
b64_sprint1_board = get_base64_image("Screenshot (569).png")
b64_sprint2_board1 = get_base64_image("Screenshot (573).png")
b64_sprint2_board2 = get_base64_image("Screenshot (574).png")
b64_sprint2_board3 = get_base64_image("Screenshot (575).png")

# Common CSS styling
css_common = """
@page {
  size: A4 portrait;
  margin: 16mm 16mm 16mm 16mm;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  color: #172b4d;
  background: #ffffff;
  line-height: 1.45;
  font-size: 9.5pt;
}
.header {
  border-bottom: 2px solid #0052cc;
  padding-bottom: 8px;
  margin-bottom: 12px;
}
.dept-title {
  font-size: 8pt;
  font-weight: 700;
  color: #5e6c84;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}
.doc-title {
  font-size: 15pt;
  font-weight: 800;
  color: #0747a6;
  margin: 3px 0 4px 0;
}
.meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  font-size: 8.5pt;
  color: #42526e;
  background: #f4f5f7;
  padding: 8px 12px;
  border-radius: 4px;
  margin-bottom: 14px;
}
.meta-grid div { margin-bottom: 2px; }
h2 {
  font-size: 11pt;
  font-weight: 700;
  color: #0747a6;
  border-bottom: 1px solid #dfe1e6;
  padding-bottom: 3px;
  margin: 12px 0 6px 0;
}
h3 {
  font-size: 10pt;
  font-weight: 600;
  color: #172b4d;
  margin: 8px 0 4px 0;
}
p {
  font-size: 9pt;
  color: #253858;
  margin-bottom: 6px;
  text-align: justify;
}
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 8.5pt;
  margin: 8px 0 12px 0;
}
th {
  background: #091e42;
  color: #ffffff;
  font-weight: 600;
  padding: 6px 8px;
  text-align: left;
  border: 1px solid #091e42;
}
td {
  padding: 6px 8px;
  border: 1px solid #dfe1e6;
  color: #253858;
  vertical-align: top;
}
tr:nth-child(even) td {
  background: #f8f9fa;
}
.badge {
  display: inline-block;
  padding: 2px 6px;
  border-radius: 3px;
  font-size: 7.5pt;
  font-weight: 700;
  text-transform: uppercase;
}
.badge-high { background: #ffebe6; color: #de350b; }
.badge-med { background: #fffae6; color: #ff8b00; }
.badge-sp { background: #ebecf0; color: #172b4d; font-weight: bold; }
.img-container {
  margin: 10px 0;
  text-align: center;
}
.img-container img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  border: 1px solid #dfe1e6;
  box-shadow: 0 2px 6px rgba(0,0,0,0.08);
}
.img-caption {
  font-size: 8pt;
  color: #6b778c;
  margin-top: 4px;
  font-style: italic;
}
.page-break {
  page-break-before: always;
}
.footer {
  border-top: 1px solid #ebecf0;
  padding-top: 6px;
  margin-top: 10px;
  font-size: 8pt;
  color: #6b778c;
  display: flex;
  justify-content: space-between;
}
.callout {
  background: #e6fcff;
  border-left: 4px solid #00a3bf;
  padding: 8px 12px;
  border-radius: 0 4px 4px 0;
  margin: 8px 0;
  font-size: 8.5pt;
}
"""

# HTML for Deliverable 1: Epics & Backlog
html_epics = f"""<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>{css_common}</style>
</head>
<body>
  <div class='header'>
    <div class='dept-title'>PES University &bull; Department of Computer Science &amp; Engineering</div>
    <div class='doc-title'>Lab 2: Agile Product Backlog &amp; Epics Specification</div>
    <div style='font-size: 9pt; color: #505f79;'>Agile Requirements Transformation, User Story Mapping &amp; Fibonacci Estimation</div>
  </div>

  <div class='meta-grid'>
    <div><strong>Student Name:</strong> Pranav</div>
    <div><strong>SRN:</strong> PES1UG24CS466</div>
    <div><strong>Problem Statement #35:</strong> Customizable Subscription Box Scheduler</div>
    <div><strong>Domain:</strong> Retail, E-Commerce &amp; Finance</div>
    <div><strong>Jira Workspace:</strong> sripranavbuduguru.atlassian.net</div>
    <div><strong>Project Key:</strong> SCRUM</div>
  </div>

  <h2>1. Overview &amp; Agile Transformation Methodology</h2>
  <p>
    In this lab, the functional requirements identified during Lab 1 for the <em>Customizable Subscription Box Scheduler</em> were transformed into Agile Epics and prioritized User Stories. Estimation was performed using the <strong>Fibonacci sequence (1, 2, 3, 5, 8...)</strong> via collaborative <strong>Planning Poker</strong> conventions, reflecting implementation complexity, technical uncertainty, and end-user business value.
  </p>

  <h2>2. Agile Epics &amp; User Stories Catalog</h2>
  <table>
    <thead>
      <tr>
        <th style='width: 14%;'>Epic / Issue Key</th>
        <th style='width: 18%;'>User Story Title</th>
        <th style='width: 38%;'>Agile User Story Format (As a... I want... So that...)</th>
        <th style='width: 8%; text-align: center;'>Points</th>
        <th style='width: 10%; text-align: center;'>Priority</th>
        <th style='width: 12%; text-align: center;'>Lab 1 Trace</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan='2'><strong>Epic 1: Subscription Box Customization</strong><br><span style='font-size: 7.5pt; color: #5e6c84;'>Personalization &amp; Swapping</span></td>
        <td><strong>SCRUM-8</strong><br>Manage Preference Tags</td>
        <td><strong>As a</strong> subscriber, <strong>I want to</strong> set and update preference tags (e.g., &ldquo;vegan&rdquo;, &ldquo;dark roast&rdquo;), <strong>so that</strong> my monthly box curates items matching my taste.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>5 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-high'>High</span></td>
        <td style='text-align: center;'>FR-002</td>
      </tr>
      <tr>
        <td><strong>SCRUM-9</strong><br>Swap Box Items</td>
        <td><strong>As a</strong> subscriber, <strong>I want to</strong> swap individual monthly box items up to 48 hours before renewal, <strong>so that</strong> I receive exactly the products I desire.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>5 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-high'>High</span></td>
        <td style='text-align: center;'>FR-001</td>
      </tr>

      <tr>
        <td rowspan='2'><strong>Epic 2: Subscription Cycle Management</strong><br><span style='font-size: 7.5pt; color: #5e6c84;'>Schedule &amp; Billing Controls</span></td>
        <td><strong>SCRUM-10</strong><br>Pause Delivery</td>
        <td><strong>As a</strong> subscriber, <strong>I want to</strong> pause recurring shipments for up to 3 months before renewal, <strong>so that</strong> I am not billed or sent boxes while traveling.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>5 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-high'>High</span></td>
        <td style='text-align: center;'>FR-001</td>
      </tr>
      <tr>
        <td><strong>SCRUM-11</strong><br>Skip Billing Cycle</td>
        <td><strong>As a</strong> subscriber, <strong>I want to</strong> skip an upcoming monthly billing cycle with auto-resumption next month, <strong>so that</strong> I don't need to permanently cancel.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>3 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-med'>Medium</span></td>
        <td style='text-align: center;'>FR-003</td>
      </tr>

      <tr>
        <td rowspan='3'><strong>Epic 3: Fulfillment &amp; Renewal Management</strong><br><span style='font-size: 7.5pt; color: #5e6c84;'>Operations &amp; Notifications</span></td>
        <td><strong>SCRUM-12</strong><br>View Fulfillment Manifest</td>
        <td><strong>As a</strong> fulfillment lead, <strong>I want to</strong> view and filter monthly box orders by category and destination, <strong>so that</strong> packing and inventory allocation are organized.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>5 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-high'>High</span></td>
        <td style='text-align: center;'>FR-004</td>
      </tr>
      <tr>
        <td><strong>SCRUM-13</strong><br>Export Fulfillment Manifest</td>
        <td><strong>As a</strong> fulfillment lead, <strong>I want to</strong> export shipping labels for 10,000 boxes in under 1 minute, <strong>so that</strong> automated warehouse packing has no delay.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>5 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-high'>High</span></td>
        <td style='text-align: center;'>FR-004, NFR-001</td>
      </tr>
      <tr>
        <td><strong>SCRUM-14</strong><br>Renewal Reminder Notifications</td>
        <td><strong>As a</strong> subscriber, <strong>I want to</strong> receive automated reminder alerts 72 hours prior to renewal date, <strong>so that</strong> I have sufficient time to customize, pause, or skip.</td>
        <td style='text-align: center;'><span class='badge badge-sp'>3 SP</span></td>
        <td style='text-align: center;'><span class='badge badge-med'>Medium</span></td>
        <td style='text-align: center;'>FR-005</td>
      </tr>
    </tbody>
  </table>

  <div class='callout'>
    <strong>Planning Poker Estimation Summary:</strong> Total Product Backlog Effort = <strong>31 Story Points</strong>.
    Sprint 1 was allocated <strong>18 Story Points</strong> (SCRUM-8, SCRUM-9, SCRUM-10, SCRUM-11) focusing on subscriber personalization and lifecycle self-service.
    Sprint 2 was allocated <strong>13 Story Points</strong> (SCRUM-12, SCRUM-13, SCRUM-14) focusing on warehouse fulfillment operations and automated notification services.
  </div>

  <h2>3. Jira Backlog &amp; Story Points Evidence</h2>
  <div class='img-container'>
    <img src='{b64_backlog}' alt='Jira Backlog and Epics View' style='max-height: 380px;' />
    <div class='img-caption'>Figure 1: Jira Agile Product Backlog showing Epics panel, Sprint 1 (18 SP), Sprint 2 (13 SP), priority indicators, and story point allocations.</div>
  </div>

  <div class='footer'>
    <span>Software Engineering Lab 2 &bull; PES University</span>
    <span>Deliverable 1: Epics &amp; Backlog Specification</span>
    <span>Pranav | PES1UG24CS466</span>
  </div>
</body>
</html>"""

# HTML for Deliverable 2: Burndown & Reflection
html_reflection = f"""<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<style>{css_common}</style>
</head>
<body>
  <div class='header'>
    <div class='dept-title'>PES University &bull; Department of Computer Science &amp; Engineering</div>
    <div class='doc-title'>Lab 2: Sprint Simulation, Burndown Chart &amp; Reflection Analysis</div>
    <div style='font-size: 9pt; color: #505f79;'>Active Sprint Simulation (To Do &rarr; In Progress &rarr; Done), Burndown Tracking &amp; Post-Sprint Reflection</div>
  </div>

  <div class='meta-grid'>
    <div><strong>Student Name:</strong> Pranav</div>
    <div><strong>SRN:</strong> PES1UG24CS466</div>
    <div><strong>Problem Statement #35:</strong> Customizable Subscription Box Scheduler</div>
    <div><strong>Simulation Timebox:</strong> 1-Week Sprint Iterations (Sprint 1 &amp; Sprint 2)</div>
    <div><strong>Committed Effort:</strong> Sprint 1: 18 SP | Sprint 2: 13 SP</div>
    <div><strong>Completion Status:</strong> 100% Completed (31 / 31 SP)</div>
  </div>

  <h2>1. Active Sprint Boards (Simulation Evidence)</h2>
  <p>
    Two distinct sprints were planned and executed in Jira. Tasks were transitioned systematically from <strong>To Do &rarr; In Progress &rarr; Done</strong> adhering to the Definition of Done (DoD).
  </p>

  <div style='display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-bottom: 8px;'>
    <div class='img-container'>
      <img src='{b64_sprint1_board}' alt='Sprint 1 Active Board' style='height: 175px; object-fit: cover;' />
      <div class='img-caption'>Figure 2: Sprint 1 Board during active simulation (SCRUM-8 to SCRUM-11).</div>
    </div>
    <div class='img-container'>
      <img src='{b64_sprint2_board2}' alt='Sprint 2 Board In Progress' style='height: 175px; object-fit: cover;' />
      <div class='img-caption'>Figure 3: Sprint 2 Board progressing tasks (SCRUM-12 to SCRUM-14).</div>
    </div>
  </div>

  <h2>2. Burndown Chart &amp; Velocity Tracking</h2>
  <div class='img-container'>
    <img src='{b64_burndown}' alt='Jira Burndown Chart' style='max-height: 290px;' />
    <div class='img-caption'>Figure 4: Jira Burndown Chart for Sprint 1 tracking remaining story points vs. ideal linear guideline.</div>
  </div>

  <h2 style='margin-top: 10px;'>3. Answers to Handout Reflection Questions</h2>

  <h3>Q1: Did your estimations reflect the actual effort?</h3>
  <p>
    <strong>Yes.</strong> Applying Planning Poker with the Fibonacci sequence (1, 2, 3, 5, 8) accurately captured the non-linear difference between tasks. Stories estimated at <strong>5 Story Points</strong> (e.g., SCRUM-9: Item Swapping, SCRUM-13: Manifest Exporting) involved critical constraints such as 48-hour cutoff lockout validation and batching 10,000 records in under 60 seconds (NFR-001). Conversely, stories estimated at <strong>3 Story Points</strong> (e.g., SCRUM-11: Skip Billing Cycle, SCRUM-14: Reminder Notifications) had straightforward state flags and notification webhooks. The team burned down all 18 points in Sprint 1 without sudden last-minute rushes, confirming estimation accuracy.
  </p>

  <h3>Q2: Was your backlog well-prioritized?</h3>
  <p>
    <strong>Yes.</strong> Backlog prioritization followed user value and technical dependency ordering. High-priority subscriber features (preference tags, box customization, pause delivery) were scheduled in <strong>Sprint 1</strong> to deliver a functional core customer journey early. Operations-heavy features (manifest viewing, batch label generation, and 72-hour reminders) were scheduled in <strong>Sprint 2</strong>, which logically builds upon finalized subscriber boxes.
  </p>

  <h3>Q3: How did your simulated sprint align with your plan?</h3>
  <p>
    <strong>Strong Alignment.</strong> The team burned down work steadily across the 7-day sprint window. SCRUM-8 completed on Day 3, SCRUM-9 on Day 5, SCRUM-10 on Day 6, and SCRUM-11 on Day 7. Sprint 2 similarly completed all 13 committed story points on schedule. Scope creep was prevented by freezing sprint backlogs once execution began.
  </p>

  <h3>Q4: What insights did the burndown chart give about your team&rsquo;s capacity?</h3>
  <p>
    The burndown chart confirmed a sustainable team velocity of <strong>15 to 18 Story Points per 1-week sprint</strong>. The curve tracked closely alongside the ideal guideline rather than displaying a flat plateau followed by a cliff-edge drop. This indicates that stories were granularly decomposed and that 18 story points is an optimal commitment threshold for future sprint planning.
  </p>

  <div class='footer'>
    <span>Software Engineering Lab 2 &bull; PES University</span>
    <span>Deliverable 2: Burndown Chart &amp; Reflection Analysis</span>
    <span>Pranav | PES1UG24CS466</span>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()

    # Generate Epics & Backlog PDF
    page1 = browser.new_page()
    page1.set_content(html_epics)
    page1.pdf(path="Lab_2_Agile_Epics_and_Backlog.pdf", format="A4", print_background=True)
    page1.close()
    print("Lab_2_Agile_Epics_and_Backlog.pdf generated.")

    # Generate Reflection & Burndown PDF
    page2 = browser.new_page()
    page2.set_content(html_reflection)
    page2.pdf(path="Lab_2_Burndown_and_Sprint_Reflection.pdf", format="A4", print_background=True)
    page2.close()
    print("Lab_2_Burndown_and_Sprint_Reflection.pdf generated.")

    # Generate Combined Complete Lab 2 Report
    html_complete = html_epics.replace("</div>\n</body>", "</div>\n<div class='page-break'></div>\n" + html_reflection.split("<body>")[1])
    page3 = browser.new_page()
    page3.set_content(html_complete)
    page3.pdf(path="Lab_2_Complete_Agile_Simulation_Report.pdf", format="A4", print_background=True)
    page3.close()
    print("Lab_2_Complete_Agile_Simulation_Report.pdf generated.")

    browser.close()
print("All Lab 2 PDFs generated successfully!")
