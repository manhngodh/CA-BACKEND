import requests

# Define job-related factors that contribute to the score
job_factors = {
    "Sport and exercise psychologist": {"biology": 0.8, "bath": 0.2, "physics": 0.2},
    "IT technical support officer": {"math": 0.5, "physics": 0.3, "foreign_language": 0.2},
    "Multimedia programmer": {"math": 0.4, "art": 0.6},
    "Child psychotherapist": {"biology": 0.3, "literature": 0.4, "art": 0.4},
    "Economist": {"math": 0.8},
    "Higher education lecturer": {"biology": 0.3, "literature": 0.2, "math": 0.1, "art": 0.2, "foreign_language": 0.2},
    "Firefighter": {"physics": 0.7},
    "Psychologist, educational": {"biology": 0.3, "literature": 0.4, "art": 0.4},
    "Armed forces logistics/support/administrative officer": {"physics": 0.6},
    "Neurosurgeon": {"biology": 0.8, "math": 0.4, "physics": 0.4},
    "Public house manager": {"math": 0.2, "art": 0.4},
    "Secretary/administrator": {"literature": 0.5, "art": 0.2},
    "Pharmacologist": {"biology": 0.8, "chemistry": 0.8},
    "Trade mark attorney": {"literature": 0.4, "art": 0.3},
    "Equality and diversity officer": {"geography": 0.5, "art": 0.2},
    "Optometrist": {"Biology": 0.6, "math": 0.3, "physics": 0.2},
    "Clinical biochemist": {"biology": 0.7, "chemistry": 0.8},
    "Engineer, production": {"math": 0.7, "physics": 0.5},
    "Paramedic": {"biology": 0.5, "physics": 0.3},
    "Secondary school teacher": {"biology": 0.3, "literature": 0.4, "art": 0.4},
    "Fast food restaurant manager": {"math": 0.3, "art": 0.3},
    # ... continue with more job titles and their corresponding factors
    # Please note that you need to manually determine the subject weight factors
}

job_earnings_data = [
    ["Sport and exercise psychologist", 80000],
    ["IT technical support officer", 72000],
    ["Multimedia programmer", 72000],
    ["Child psychotherapist", 95000],
    ["Economist", 65000],
    ["Higher education lecturer", 93000]
    # ... other job data ...
]


def get_job_earnings_data():
    try:
        response = requests.get("http://stats:5000/job_earnings")
        response.raise_for_status()  # Raise an exception for HTTP errors
        job_earnings_data = response.json()
        return job_earnings_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching job earnings data: {e}")
        return []

def recommend_jobs(school_performance_scores, top_n=3):
    recommended_jobs = []

    job_earnings_data = get_job_earnings_data()

    for job_title, factors in job_factors.items():
        compatibility_score = sum(
            weight_factor * school_performance_scores.get(subject, 0)
            for subject, weight_factor in factors.items()
        )

        salary = next((job_data[1] for job_data in job_earnings_data if job_data[0] == job_title), 0)

        recommended_jobs.append({
            "job_title": job_title,
            "compatibility_score": compatibility_score,
            "salary": salary
        })

    recommended_jobs.sort(key=lambda x: x["compatibility_score"], reverse=True)
    return recommended_jobs[:top_n]


if __name__ == '__main__':
    # Example usage:
    school_performance_scores = {
        "math": 90,
        "physics": 85,
        "chemistry": 78,
        "biology": 92,
        "literature": 88,
        "history": 76,
        "geography": 82,
        "philosophy": 95,
        "art": 80,
        "foreign_language": 92
    }

    recommended_jobs = recommend_jobs(school_performance_scores)
    print("Recommended Jobs:", recommended_jobs)

