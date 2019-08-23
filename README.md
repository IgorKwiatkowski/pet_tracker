# pet_tracker
Simple Django app for tracking my pets' food and meds

Hello and thank you for having a look at my first "serious" project. It was a graduation project for my Python Back End Developer course at Coders Lab.

I wrote this program because I needed a tool for tracking my five pets, each with their separate food and meds in different dosages, applied on different days in different intervals. This basic functionality runs fine with a small database.

Is it deployed, can I see it in action?
I have the app deployed on Heroku for personal use. I would love to deploy it for public in the future.

Why is there no full CRUD for all the pets, products?
I wanted to keep the app clean and simple, as it is mostly accessed on mobile. I decided that less is more, and so there are no pet update or product update views, as they would be rarely used.

Are there logins, user accounts etc?
There are no user accounts or any related features, because the program's intended use is mostly just for my wife and myself.

How can I see days other than today or tomorrow?
In everyday use the "today" view is by far the most important, so this feature is not high on the list. You can pass the date into the URL in /day/YYYY/MM/DD format.

![Today view](https://github.com/IgorKwiatkowski/pet_tracker/tree/screenshots/screenshots/today_view.png?raw=true "Today View")
