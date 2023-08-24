
def recommend_jobs(school_performance):
    job_earnings_data = [
        ["Sport and exercise psychologist", 80000],
        ["IT technical support officer", 72000],
        ["Multimedia programmer", 72000],
        ["Child psychotherapist", 95000],
        ["Economist", 65000],
        ["Higher education lecturer", 93000]
        # ... other job data ...
    ]

    # Calculate a score for each job based on school performance
    job_scores = []
    for job, earnings in job_earnings_data:
        score = calculate_score(school_performance, job)
        job_scores.append((job, score))

    # Sort jobs by score in descending order
    sorted_jobs = sorted(job_scores, key=lambda x: x[1], reverse=True)

    # Select the top 3 recommended jobs
    recommended_jobs = [job for job, _ in sorted_jobs[:3]]

    return recommended_jobs

# Example usage
school_performance = {
    "Math": 85,
    "Physics": 70,
    "Chemistry": 75,
    # ... other subjects ...
}

recommended_jobs = recommend_jobs(school_performance)
print("Recommended Jobs:", recommended_jobs)



def calculate_score(school_performance, job):
    # Define weights for each subject (you can adjust these based on importance)
    subject_weights = {
        "Math": 0.3,
        "Physics": 0.2,
        "Chemistry": 0.2,
        "Biology": 0.1,
        "Literature": 0.1,
        "History": 0.1,
        "Geography": 0.1,
        "Philosophy": 0.1,
        "Art": 0.1,
        "Foreign Language": 0.2
    }

    # Define job-related factors that contribute to the score
    job_factors = {
        "Sport and exercise psychologist": {"earnings": 80000, "require_math": False},
        "IT technical support officer": {"earnings": 72000, "require_math": True},
        "Multimedia programmer": {"earnings": 72000, "require_math": True},
        "Child psychotherapist": {"earnings": 95000, "require_math": False},
        "Economist": {"earnings": 65000, "require_math": True},
        "Higher education lecturer": {"earnings": 93000, "require_math": False}
        # ... other job factors ...
    }

    # Calculate the weighted average of subject scores
    weighted_score = sum(
        school_performance.get(subject, 0) * weight
        for subject, weight in subject_weights.items()
    )

    # Apply job-specific factors (e.g., requiring specific subjects)
    job_data = job_factors.get(job, {})
    if job_data.get("require_math") and school_performance.get("Math", 0) < 70:
        return 0  # Skip job if it requires math and score is too low

    # Calculate the final score as a combination of school performance and job factors
    final_score = weighted_score + job_data.get("earnings", 0)

    return final_score

# Example usage
school_performance = {
    "Math": 85,
    "Physics": 70,
    "Chemistry": 75,
    # ... other subjects ...
}

job = "IT technical support officer"
score = calculate_score(school_performance, job)
print("Score for job", job, ":", score)
