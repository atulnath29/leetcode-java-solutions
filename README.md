# 🚀 LeetCode Java Solutions — Daily DSA Streak

Welcome to my **LeetCode Java Solutions Repository** 👨‍💻

This repository contains my **daily LeetCode problem solutions in Java**, uploaded consistently to maintain my coding streak and strengthen my Data Structures & Algorithms skills.

---

## 📌 About This Repository

* 🔥 Daily LeetCode Streak Maintenance
* ☕ All solutions written in **Java**
* 🧠 Focus on **DSA & Problem Solving**
* 📈 Tracking consistency & growth
* 💼 Helpful for **placements & portfolio**

---

## 🛠️ Tech Stack

* **Language:** Java
* **Concepts Covered:**

  * Arrays
  * Strings
  * Linked List
  * Stack & Queue
  * Trees
  * Graphs
  * Dynamic Programming
  * Recursion & Backtracking

---

## 📂 Folder Structure

```
leetcode-java-solutions/

├── Easy/
├── Medium/
├── Hard/
└── Daily-Challenge/
```

* **Easy/** → Beginner friendly problems
* **Medium/** → Interview level problems
* **Hard/** → Advanced DSA problems
* **Daily-Challenge/** → LeetCode daily problems

---

## 📝 Solution Format

Each solution file contains:

* ✅ Problem Name
* ✅ LeetCode Problem Link
* ✅ Approach / Explanation
* ✅ Time Complexity
* ✅ Space Complexity
* ✅ Clean Java Code

---

## 📅 Daily Streak Tracker

| Day | Problem                                        | Difficulty | Solution |
| --- | ---------------------------------------------- | ---------- | -------- |
| 1   | Two Sum                                        | Easy       | Java     |
| 2   | Add Two Numbers                                | Medium     | Java     |
| 3   | Longest Substring Without Repeating Characters | Medium     | Java     |

*(Updating Daily…)*

---

## 🧠 Example Solution Structure

```java
// Problem: Two Sum
// Link: https://leetcode.com/problems/two-sum/
// Difficulty: Easy

import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (map.containsKey(diff)) {
                return new int[]{map.get(diff), i};
            }

            map.put(nums[i], i);
        }

        return new int[]{};
    }
}
```

---

## 🎯 My Goals

* Solve **500+ LeetCode Problems**
* Master **DSA in Java**
* Crack **Product-Based Companies**
* Maintain **365-Day Coding Streak**

---

## 📊 Progress Tracker

| Difficulty | Solved |
| ---------- | ------ |
| Easy       | 0      |
| Medium     | 0      |
| Hard       | 0      |

*(Auto-updated manually)*

---

## 🌟 Why This Repo Matters

This repository represents my:

* Consistency 📈
* Coding Discipline ⏳
* Java Expertise ☕
* Interview Preparation 💼

---

## 🤝 Contribution

This is a personal streak repository, but suggestions are always welcome.

If you find this helpful, feel free to ⭐ the repo.

---

## 📬 Connect With Me

* GitHub: **atulnath29**
* LeetCode: *(Add your profile link)*

---

### ⭐ Don’t forget to Star this Repository if you like it!

Happy Coding 🚀
