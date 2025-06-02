# PlanBee
<h1>
  🐝📝 PlanBee: Your Smart Scheduling Companion
</h1>

<h2>
  Description
</h2>
<p>
  <b>PlanBee</b> is a modern, user-friendly Python application designed to streamline scheduling and reminders for busy individuals and teams. With its intuitive interface, PlanBee manages your daily events, automates reminders, and keeps your schedule organized and accessible. Users can create, view, edit, and delete events, receive timely email notifications, and maintain a comprehensive record of their activities.
  <br><br>
  Our mission with PlanBee is to empower users to take control of their time and tasks, reducing stress and boosting productivity with a reliable, efficient, and enjoyable scheduling experience.
</p>

<h2>
  Key Features:
</h2>
<p>
📅 Effortless Event Scheduling<br>
⏰ Automated Email Reminders<br>
🔑 Secure OTP-Based Login & Registration<br>
🗂️ Comprehensive Event & Profile Database<br>
📝 Easy Editing & Deletion of Events<br>
📊 Real-Time Overview of Schedules<br>
🖥️ Clean, Emoji-Enhanced Command-Line Interface<br>
🔒 Robust Exception Handling & Data Security<br>
</p>
<p>
  With PlanBee, you can manage your time efficiently, never miss an important event, and enjoy peace of mind knowing your schedule is always at your fingertips.
</p>

<h2>
  💡 Why was PlanBee created?
</h2>
<p>
  In today’s fast-paced world, managing schedules and remembering important events can be overwhelming. Missed appointments, forgotten tasks, and scattered notes can lead to stress and lost opportunities. PlanBee was created to solve these challenges by providing a centralized, automated, and user-friendly solution for all your scheduling needs.
  <h3>
   🔧 Problems it solves
  </h3>
  <ol>
    <b><li>No More Missed Events:</li></b>
    Automated reminders ensure you’re always on time for meetings, deadlines, and personal commitments.<br><br>
    <b><li>Centralized Schedule Management:</li></b>
    All your events and tasks are stored in one place, easily accessible and searchable.<br><br>
    <b><li>Secure & Hassle-Free Access:</li></b>
    OTP-based login and registration keep your data safe and make access simple.<br><br>
    <b><li>Efficient Data Handling:</li></b>
    PlanBee’s robust backend manages large volumes of events and user profiles without slowing down.<br>
  </ol>
  <br>
  PlanBee isn’t just for individuals—it’s perfect for teams, students, professionals, and anyone who values their time. By automating reminders and organizing schedules, PlanBee helps you focus on what matters most.
</p>

<h2>
  Learning Outcomes 📚
</h2>
<p>
  🔄 Scalable use of user-defined functions<br>
  ⚙️ Importance of modular programming in large projects<br>
  🤝 Collaboration using GitHub, Git Bash, and VS Code<br>
  📊 Practical use of data structures and types<br>
  🛠️ Building robust algorithms for real-world applications<br>
  📧 Integrating email and notification systems<br>
</p>

<h2>
  How to Use? 🤔
</h2>
<p>
<ol>
  <li>Clone or download the repository to your local machine.</li>
  <li>Install required dependencies:<br>
    <code>pip install mysql-connector-python psutil</code>
  </li>
  <li>Ensure your MySQL server is running and accessible.</li>
  <li>Configure your database credentials in <code>head/main.py</code> if needed.</li>
  <li>Run the application:<br>
    <code>python head/main.py</code>
  </li>
  <li>Follow the on-screen instructions to register, log in, and manage your schedules.</li>
</ol>
</p>

<h2>
  🗂️ Project Structure
</h2>
<pre>
New_project_work/
│
├── head/
│   └── main.py                <i>Main control flow, menus, and user session management</i>
│
├── create_profile/
│   ├── index_1.py             <i>User registration, validation, and OTP handling</i>
│   ├── mail_on_register.py    <i>Sends registration confirmation emails</i>
│   └── otp_ver.py             <i>OTP generation, validation, and resend logic</i>
│
├── login/
│   └── main.py                <i>User login and authentication</i>
│
├── schedules/
│   ├── main.py                <i>Create new schedules/events</i>
│   ├── view_schedules.py      <i>View all scheduled events</i>
│   ├── edit_schedules.py      <i>Edit existing events</i>
│   └── delete_upcoming_events.py <i>Delete future events</i>
│
├── tools/
│   ├── connection.py          <i>Database connection utilities</i>
│   ├── exists.py              <i>Checks for existing users/events</i>
│   ├── pull_data.py           <i>Fetches user/event data</i>
│   └── Mail/
│       ├── notify_mail.py     <i>Sends event reminder emails</i>
│       ├── otp_mail.py        <i>Sends OTP emails</i>
│       └── main.py            <i>Mail sending logic</i>
│
├── notification/
│   └── main.py                <i>Handles background notification processes</i>
│
├── LICENSE                    <i>MIT License</i>
└── README.md                  <i>This file</i>
</pre>

<h2>
  📝 Example CLI Output
</h2>
<pre>
============================================================
                🐝📝  Welcome to PlanBee  🐝📝
                Your Smart Scheduling Companion
============================================================

🆕 1. Create Profile
🔑 2. Login
❌ 3. Exit

Please enter your choice: 
</pre>

<h2>
  📦 Requirements
</h2>
<ul>
  <li>Python 3.8+</li>
  <li>MySQL Server</li>
  <li>Required Python packages: <code>mysql-connector-python</code>, <code>psutil</code></li>
</ul>

<h2>
  👨‍💻 Authors
</h2>
<ul>
  <li><b>Aayush Talukdar</b></li>
  <li><b>Priyanshu Mohanty</b></li>
</ul>

<h2>
  📄 License
</h2>
<p>
  This project is licensed under the <b>MIT License</b>.<br>
  See the <a href="LICENSE">LICENSE</a> file for details.
</p>
