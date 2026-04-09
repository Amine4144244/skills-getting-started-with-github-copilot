def test_get_activities_returns_all_activity_details(client):
    # Arrange
    expected_activity_name = "Chess Club"
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity_name in activities

    activity = activities[expected_activity_name]
    assert expected_keys.issubset(activity.keys())
    assert activity["description"] == "Learn strategies and compete in chess tournaments"
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert isinstance(activity["participants"], list)
    assert "michael@mergington.edu" in activity["participants"]