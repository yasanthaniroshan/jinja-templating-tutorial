**Profile Details**

- **Full Name:** {{ names | map('upper') | join(' ') }}
- **Date of Birth:** {{ "%s-%s-%s" | format(date,month,year) }}

