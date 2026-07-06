class Weather:
    @staticmethod
    def get_weather(city, MakeRequest):
        locs = {"manchester": "53.4808,-2.2426", "vaasa": "63.0902,21.6156", "winchester": "51.0632,-1.3080"}
        if city.lower() not in locs:
            return f"City not found. Try {list(locs.keys())}"

        url = "https://api.open-meteo.com/v1/"
        lat = locs.get(city.lower()).split(",")[0]
        long = locs.get(city.lower()).split(",")[1]

        request = MakeRequest(f"{url}forecast?latitude={lat}&longitude={long}&current_weather=true")
        request = request.make_request()
        data = request.json()
        return data