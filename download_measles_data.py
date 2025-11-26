"""
Script to download measles data from UKHSA API
This downloads initial data for the dashboard
"""
import requests
import time
import json

class APIwrapper:
    # class variables shared among all instances
    _access_point="https://api.ukhsa-dashboard.data.gov.uk"
    _last_access=0.0 # time of last api access

    def __init__(self, theme, sub_theme, topic, geography_type, geography, metric):
        """ Init the APIwrapper object, constructing the endpoint from the structure
        parameters """
        url_path=(f"/themes/{theme}/sub_themes/{sub_theme}/topics/{topic}/geography_types/" +
                  f"{geography_type}/geographies/{geography}/metrics/{metric}")
        self._start_url=APIwrapper._access_point+url_path
        self._filters=None
        self._page_size=-1
        self.count=None

    def get_page(self, filters={}, page_size=5):
        """ Access the API and download the next page of data """
        if page_size>365:
            raise ValueError("Max supported page size is 365")
        if filters!=self._filters or page_size!=self._page_size:
            self._filters=filters
            self._page_size=page_size
            self._next_url=self._start_url
        if self._next_url==None:
            return []
        curr_time=time.time()
        deltat=curr_time-APIwrapper._last_access
        if deltat<0.33:
            time.sleep(0.33-deltat)
        APIwrapper._last_access=curr_time
        parameters={x: y for x, y in filters.items() if y!=None}
        parameters['page_size']=page_size
        response = requests.get(self._next_url, params=parameters).json()
        self._next_url=response['next']
        self.count=response['count']
        return response['results']

    def get_all_pages(self, filters={}, page_size=365):
        """ Access the API and download all available data pages """
        data=[]
        while True:
            next_page=self.get_page(filters, page_size)
            if next_page==[]:
                break
            data.extend(next_page)
        return data

# Define structure for measles data
structure={"theme": "infectious_disease",
           "sub_theme": "vaccine_preventable",
           "topic": "Measles",
           "geography_type": "Nation",
           "geography": "England"}

print("Downloading measles data from UKHSA API...")
print("This may take a few minutes...")

# Download cases by week
print("\n1. Downloading weekly cases...")
structure["metric"]="Measles_testing_positivityByWeek"
try:
    api=APIwrapper(**structure)
    measles_weekly_cases=api.get_all_pages()
    print(f"   Downloaded {len(measles_weekly_cases)} data points")
    with open("measles_weekly_cases.json", "wt") as outf:
        json.dump(measles_weekly_cases, outf)
    print("   Saved to measles_weekly_cases.json")
except Exception as e:
    print(f"   Error: {e}")
    measles_weekly_cases = []

# Download age distribution
print("\n2. Downloading age distribution...")
structure["metric"]="Measles_cases_countByWeek"
try:
    api=APIwrapper(**structure)
    measles_age_dist=api.get_all_pages()
    print(f"   Downloaded {len(measles_age_dist)} data points")
    with open("measles_age_dist.json", "wt") as outf:
        json.dump(measles_age_dist, outf)
    print("   Saved to measles_age_dist.json")
except Exception as e:
    print(f"   Error: {e}")
    measles_age_dist = []

print("\nData download complete!")
print(f"Total data points: {len(measles_weekly_cases) + len(measles_age_dist)}")
