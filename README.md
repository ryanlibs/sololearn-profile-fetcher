# sololearn-profile-fetcher
A Python script to fetch user profile information from [Sololearn](https://www.sololearn.com).

![MIT License](https://img.shields.io/badge/license-MIT-green)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/ryanlibs/sololearn-profile-fetcher)
![Issues](https://img.shields.io/github/issues/ryanlibs/sololearn-profile-fetcher)

# Features

## User Profile
- Retrieve detailed user information including:
  - User ID, name, avatar, and bio.
  - User's registration date and country code.
  - Access level, badges, and XP progress.
  - Follower and following count.

## Course Progress
 - Track progress for courses a user is enrolled in:
  - Course name, icon, and completion status.
  - Last progress update and percentage completed.

## Certificates
- Access earned certificates with details:
  - Certificate name, associated course, and start date.
  - Downloadable links for PDF and PNG formats.
  - Shareable URLs for showcasing achievements.

## Code Bits
- View user-created code projects with:
  - Programming language used.
  - Public visibility and last modified date.
  - Unique public IDs for sharing.

## Goals and Streaks
- Monitor user goals and progress:
  - Target values and current completion levels.
  - Daily streak counts and historical streak data.

and more...

## Usage
Endpoint:
```sh
https://sololearn-api.replit.app/?profile=<profile_id>
```
Example:
```sh
https://sololearn-api.replit.app/?profile=33173273
```

OR

Run the script with the profile ID of the user whose data you want to fetch:

```bash
python main.py <profile_id>
```

Example:

```bash
python main.py 33173273
```

## Output 

```json
{
  "userDetails": {
    "id": "profileID",
    "name": "name",
    "email": null,
    "avatarUrl": "avatarUrl",
    "accessLevel": 0,
    "badge": "badge",
    "badges": [
      {
        "name": "badgeName",
        "priority": "badgePriority"
      }
    ],
    "level": "userLevel",
    "xp": "userXP",
    "countryCode": "countryCode",
    "isPro": "isPro",
    "isFirstVisitAfterTrialAsPro": false,
    "followers": "followerCount",
    "following": "followingCount",
    "isFollowing": false,
    "bio": "bio",
    "registerDate": "registerDate",
    "connectedAccounts": [
      {
        "connectionId": "connectionID",
        "service": "serviceName",
        "name": "accountName",
        "profileUrl": null,
        "isVisible": true,
        "syncDate": null,
        "avatarUrl": "accountAvatarUrl"
      }
    ]
  },
  "coursesProgress": [
    {
      "courseId": "courseID",
      "courseName": "courseName",
      "courseIconURL": "courseIconURL",
      "courseColor": "courseColor",
      "isCompleted": "isCompleted",
      "lastProgressDate": "lastProgressDate",
      "progress": "progressValue",
      "isLearnEngineCourse": "isLearnEngineCourse",
      "alias": null,
      "statusId": "statusID"
    }
  ],
  "certificates": [
    {
      "courseId": "courseID",
      "name": "certificateName",
      "courseColor": "courseColor",
      "iconURL": "iconURL",
      "startDate": "startDate",
      "expireDate": null,
      "url": "certificatePDFUrl",
      "imageUrl": "certificateImageUrl",
      "uncompleteUrl": null,
      "shareUrl": "shareUrl"
    }
  ],
  "userGoals": [],
  "userStreak": {
    "streak": "streakCount",
    "streakDate": "streakDate"
  },
  "codeCoaches": null,
  "userBadges": null,
  "userCodes": [
    {
      "id": "id",
      "publicId": "publicId",
      "language": "language",
      "name": "name",
      "isPublic": "isPublic",
      "modifiedDate": "modifiedDate"
    }
  ],
  "userGoalProgress": [
    {
      "id": "id",
      "userGoalId": "userGoalId",
      "currentValue": "currentValue",
      "targetValue": "targetValue",
      "localDate": "localDate",
      "date": "date"
    }
  ],
  "userLessonGoals": [
    {
      "id": "id",
      "userId": "userId",
      "goalType": "goalType1",
      "goalValue": "goalValue",
      "origin": "origin",
      "localDate": "localDate",
      "date": "date"
    }
  ],
  "userDailyStreak": {
    "dailyStreakCount": "dailyStreakCount",
    "dailyStreaks": [
      {
        "status": "dailyStreakStatus"
      }
    ]
  },
  "groupSubscription": null
}
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have ideas or fixes.

## Support

If you find this script useful and want to support my caffeine addiction, please consider buying me a coffee! ☕😁

[![Buy Me a Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-orange?logo=buymeacoffee)](https://www.buymeacoffee.com/ryanlibs)
