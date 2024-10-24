import math

def compute_HRV(interval1: float, interval2: float, interval3: float) -> float:
    """
    Compute heart rate variability (HRV).
    Parameters:
        interval1, interval2, and interval3: three successive heartbeat intervals, in ms.
    Returns:
        The heart rate variability.
    """
    return math.sqrt(((interval1 - interval2) ** 2 + (interval2 - interval3) ** 2) / 2)

def temperature_is_fever(temperature: float, site: str) -> bool:
    """
    Determines whether a given temperature and test site represents fever.
    Parameters:
        temperature: the recorded temperature in °C.
        site: either "oral" or "underarm".
    Returns:
        True if the temperature indicates a fever.
    """
    fever_criteria = {
        'oral': 37.8,
        'underarm': 37.2
    }
    return temperature >= fever_criteria[site]

def has_fever() -> bool:
    """
    Asks the user for their body temperature and where it was measured,
    and returns True if they have a fever.
    """
    temperature = float(input("Enter your temperature (°C): "))
    site = input("Was the temperature measured Orally (O) or Underarm (U)? (enter O or U): ").lower()
    site_location = {
        'o': "oral",
        'u': "underarm"
    }
    site = site_location.get(site, 'oral') 
    return temperature_is_fever(temperature, site)

def has_nausea() -> bool:
    """
    Asks the user if they are experiencing nausea and returns their response.
    """
    return input("Are you experiencing nausea? (enter y or n): ").lower() == 'y'

def has_low_HRV() -> bool:
    """
    Asks the user to enter three successive heartbeat intervals in ms.
    Returns True if the HRV is less than 50 ms.
    """
    print("\nPlease enter 3 heartbeat intervals in ms…")
    interval1 = float(input("Enter first interval: "))
    interval2 = float(input("Enter second interval: "))
    interval3 = float(input("Enter third interval: "))
    return compute_HRV(interval1, interval2, interval3) < 50

def has_high_cortisol() -> bool:
    """
    Asks the user to enter their cortisol level and returns True if the level is above 25.0 mcg/dL.
    """
    cortisol_level = float(input("\nEnter cortisol level in mcg/dL: "))
    return cortisol_level > 25.0

def diagnose_flu():
    print("\nDiagnosis: Flu")

def diagnose_infection():
    print("\nDiagnosis: Infection")

def diagnose_stress():
    print("\nDiagnosis: Stress")

def diagnose_healthy():
    print("\nDiagnosis: Healthy")

def process_nausea(nausea_result):
    """
    Handles nausea decision and diagnoses flu or infection.
    """
    functions = [diagnose_infection, diagnose_flu]
    functions[nausea_result]()

def process_cortisol(cortisol_result):
    """
    Handles cortisol decision and diagnoses stress or healthy.
    """
    functions = [diagnose_healthy, diagnose_stress]
    functions[cortisol_result]()

def check_cortisol():
    """
    Checks cortisol and processes the cortisol decision.
    """
    cortisol_result = has_high_cortisol()
    process_cortisol(cortisol_result)

def process_hrv(hrv_result):
    """
    Handles HRV decision and continues to cortisol check or healthy diagnosis.
    """
    functions = [diagnose_healthy, check_cortisol]
    functions[hrv_result]()

def start_with_fever():
    """
    Handles the path where the user has a fever.
    """
    nausea = has_nausea()
    process_nausea(nausea)

def start_without_fever():
    """
    Handles the path where the user does not have a fever.
    """
    low_hrv = has_low_HRV()
    process_hrv(low_hrv)

def process_fever(fever_result):
    """
    Decides whether to handle the fever path or the non-fever path.
    """
    functions = [start_without_fever, start_with_fever]
    functions[fever_result]()

def main() -> None:
    """
    Runs the diagnostic program and prints out the final diagnosis.
    """
    fever = has_fever()
    process_fever(fever)

main()