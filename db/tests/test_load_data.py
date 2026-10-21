from db.load_data import load_json_data

def test_load_json_data_loads_correctly():
    filename = "venues.json"
    expected = [{
                    "name": "Nexus, University of Leeds",
                    "address": "Discovery Way, Leeds, LS2 3AA",
                    "capacity": 200
                },
                {
                    "name": "Manchester Central Library",
                    "address": "St Peter's Square, Manchester, M2 5PD",
                    "capacity": 80
                },
                {
                    "name": "Online – Zoom",
                    "address": None,
                    "capacity": 500
                },
                {
                    "name": "The Skiff",
                    "address": "30 Cheapside, Brighton, BN1 4GD",
                    "capacity": 60
                },
                {
                    "name": "Newspeak House",
                    
                    "address": "133 Bethnal Green Road, London, E2 7DG",
                    "capacity": 120
                }]
    result = load_json_data(filename)

    assert result == expected