import requests
from bs4 import BeautifulSoup
import re
import json
from datetime import datetime
from deep_translator import GoogleTranslator


def get_table_value(soup, label):
    """Find <dt>label</dt><dd>value</dd>"""
    dt = soup.find("dt", string=re.compile(label))
    if dt and dt.find_next_sibling("dd"):
        return dt.find_next_sibling("dd").get_text(strip=True)
    return None

def get_table_thtd_value(soup, label):
    """
    Find <th>label</th><td>value</td>
    - Hỗ trợ label = string hoặc list các string
    """
    if isinstance(label, (list, tuple)):
        for l in label:
            th = soup.find("th", string=re.compile(l))
            if th and th.find_next_sibling("td"):
                return th.find_next_sibling("td").get_text(strip=True)
    else:
        th = soup.find("th", string=re.compile(label))
        if th and th.find_next_sibling("td"):
            return th.find_next_sibling("td").get_text(strip=True)
    return None


def translate_text(text, target_lang):
    """Translate text if not None"""
    if not text:
        return None
    try:
        return GoogleTranslator(source="ja", target=target_lang).translate(text)
    except Exception:
        return None


def parse_property(url):
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "html.parser")

    data = {
        "link": url,
        "property_csv_id": url.split("/")[-1],
        "postcode": None,
        "prefecture": None,
        "city": None,
        "district": None,
        "chome_banchi": None,
        "building_type": None,
        "year": None,
        "building_name_ja": None,
        "building_name_en": None,
        "building_name_zh_CN": None,
        "building_name_zh_TW": None,
        "building_description_en": None,
        "building_description_ja": None,
        "building_description_zh_CN": None,
        "building_description_zh_TW": None,
        "building_landmarks_en": None,
        "building_landmarks_ja": None,
        "building_landmarks_zh_CN": None,
        "building_landmarks_zh_TW": None,
        "layout": None,
        "station_name_1": None,
        "train_line_name_1": None,
        "walk_1": None,
        "bus_1": None,
        "car_1": None,
        "cycle_1": None,
        "station_name_2": None,
        "train_line_name_2": None,
        "walk_2": None,
        "bus_2": None,
        "car_2": None,
        "cycle_2": None,
        "station_name_3": None,
        "train_line_name_3": None,
        "walk_3": None,
        "bus_3": None,
        "car_3": None,
        "cycle_3": None,
        "station_name_4": None,
        "train_line_name_4": None,
        "walk_4": None,
        "bus_4": None,
        "car_4": None,
        "cycle_4": None,
        "station_name_5": None,
        "train_line_name_5": None,
        "walk_5": None,
        "bus_5": None,
        "car_5": None,
        "cycle_5": None,
        "map_lat": None,
        "map_lng": None,
        "num_units": None,
        "floors": None,
        "basement_floors": None,
        "parking": None,
        "parking_cost": None,
        "bicycle_parking": None,
        "motorcycle_parking": None,
        "structure": None,
        "building_notes": None,
        "building_style": None,
        "autolock": None,
        "credit_card": None,
        "concierge": None,
        "delivery_box": None,
        "elevator": None,
        "gym": None,
        "newly_built": None,
        "pets": None,
        "swimming_pool": None,
        "ur": None,
        "room_type": None,
        "size": None,
        "unit_no": None,
        "ad_type": None,
        "available_from": None,
        "property_description_en": None,
        "property_description_ja": None,
        "property_description_zh_CN": None,
        "property_description_zh_TW": None,
        "property_other_expenses_en": None,
        "property_other_expenses_ja": None,
        "property_other_expenses_zh_CN": None,
        "property_other_expenses_zh_TW": None,
        "featured_a": None,
        "featured_b": None,
        "featured_c": None,
        "floor_no": None,
        "monthly_rent": None,
        "monthly_maintenance": None,
        "months_deposit": None,
        "numeric_deposit": None,
        "months_key": None,
        "numeric_key": None,
        "months_guarantor": None,
        "numeric_guarantor": None,
        "months_agency": None,
        "numeric_agency": None,
        "months_renewal": None,
        "numeric_renewal": None,
        "months_deposit_amortization": None,
        "numeric_deposit_amortization": None,
        "months_security_deposit": None,
        "numeric_security_deposit": None,
        "lock_exchange": None,
        "fire_insurance": None,
        "other_initial_fees": None,
        "other_subscription_fees": None,
        "no_guarantor": None,
        "guarantor_agency": None,
        "guarantor_agency_name": None,
        "rent_negotiable": None,
        "renewal_new_rent": None,
        "lease_date": None,
        "lease_months": None,
        "lease_type": None,
        "short_term_ok": None,
        "balcony_size": None,
        "property_notes": None,
        "facing_north": None,
        "facing_northeast": None,
        "facing_east": None,
        "facing_southeast": None,
        "facing_south": None,
        "facing_southwest": None,
        "facing_west": None,
        "facing_northwest": None,
        "aircon": None,
        "aircon_heater": None,
        "all_electric": None,
        "auto_fill_bath": None,
        "balcony": None,
        "bath": None,
        "bath_water_heater": None,
        "blinds": None,
        "bs": None,
        "cable": None,
        "carpet": None,
        "cleaning_service": None,
        "counter_kitchen": None,
        "dishwasher": None,
        "drapes": None,
        "female_only": None,
        "fireplace": None,
        "flooring": None,
        "full_kitchen": None,
        "furnished": None,
        "gas": None,
        "induction_cooker": None,
        "internet_broadband": None,
        "internet_wifi": None,
        "japanese_toilet": None,
        "linen": None,
        "loft": None,
        "microwave": None,
        "oven": None,
        "phoneline": None,
        "range": None,
        "refrigerator": None,
        "refrigerator_freezer": None,
        "roof_balcony": None,
        "separate_toilet": None,
        "shower": None,
        "soho": None,
        "storage": None,
        "student_friendly": None,
        "system_kitchen": None,
        "tatami": None,
        "underfloor_heating": None,
        "unit_bath": None,
        "utensils_cutlery": None,
        "veranda": None,
        "washer_dryer": None,
        "washing_machine": None,
        "washlet": None,
        "western_toilet": None,
        "yard": None,
        "youtube": None,
        "vr_link": None,
        "floorplan": None,
        "numeric_guarantor_max": None,
        "discount": None,
        "create_date": datetime.now().isoformat(),
    }

    # Building name / type / structure
    data["building_name_ja"] = get_table_value(soup, "物件名")

    if data["building_name_ja"]:
        data["building_name_en"] = translate_text(data["building_name_ja"], "en")
        data["building_name_zh_CN"] = translate_text(data["building_name_ja"], "zh-CN")
        data["building_name_zh_TW"] = translate_text(data["building_name_ja"], "zh-TW")

    data["building_type"] = get_table_value(soup, "種別")
    data["structure"] = get_table_value(soup, "建物構造")

    # Address
    addr = get_table_value(soup, "所在地")
    if addr:
        m = re.match(r"(.{3})(.+区)(.+)", addr)
        if m:
            data["prefecture"] = m.group(1)
            data["city"] = m.group(2)
            data["district"] = m.group(3)
            data["chome_banchi"] = m.group(2) + m.group(3)

    # Year built
    year_text = get_table_value(soup, "築年月")
    if year_text:
        m = re.search(r"(\d{4})年", year_text)
        if m:
            data["year"] = m.group(1)

    # Room type / size / rent
    data["room_type"] = get_table_value(soup, "間取り")

    size_text = get_table_value(soup, "専有面積")
    if size_text:
        m = re.search(r"([\d.]+)", size_text)
        if m:
            data["size"] = float(m.group(1))


    rent_text = get_table_value(soup, "賃料")
    if rent_text:
        m = re.search(r"([\d.]+)万円", rent_text.replace(",", ""))
        if m:
            value = float(m.group(1)) * 10000            
            data["monthly_rent"] = f"{int(value):,}円"

    # --- Access ---
    access_dt = soup.find("dt", string=lambda t: t and "交通" in t)
    if access_dt:
        dd = access_dt.find_next_sibling("dd")
        if dd:
            for idx, li in enumerate(dd.select("li"), 1):
                text = li.get_text(strip=True)
                m = re.match(r"(.+?)/(.+?)駅 徒歩(\d+)分", text)
                if m:
                    line = m.group(1).strip()
                    station = m.group(2).strip()
                    walk = int(m.group(3))
                    data[f"train_line_name_{idx}"] = line
                    data[f"station_name_{idx}"] = station
                    data[f"walk_{idx}"] = walk

    # Unit number
    unit_text = get_table_thtd_value(soup, ["号室", "部屋番号"])
    if unit_text:
        data["unit_no"] = unit_text

    # Floor info
    floor_text = get_table_thtd_value(soup, "所在階")
    if floor_text:
        m = re.match(r"(\d+)階/(\d+)階建", floor_text)
        if m:
            data["floor_no"] = int(m.group(1))
            data["floors"] = int(m.group(2))

    # Layout (remove Bタイプ etc.)
    layout_text = get_table_thtd_value(soup, "間取り")
    if layout_text:
        clean_layout = re.sub(r"（.*?）", "", layout_text).strip()
        data["layout"] = clean_layout

    # Monthly maintenance 
    maint_text = get_table_thtd_value(soup, ["管理費・共益費", "管理費", "共益費"])
    if maint_text:
        # Trường hợp "xxxx円"
        m = re.search(r"([\d,]+)円", maint_text)
        if m:
            value = int(m.group(1).replace(",", ""))
            data["monthly_maintenance"] = f"{value:,}円"
        else:
            # Trường hợp "x万円" (có thể có thập phân)
            m = re.search(r"([\d\.]+)万", maint_text)
            if m:
                value = float(m.group(1)) * 10000
                data["monthly_maintenance"] = f"{int(value):,}円"



    # Discount (フリーレント…)
    discount_text = get_table_thtd_value(soup, "フリーレント")
    if discount_text:
        data["discount"] = discount_text

    # Fire insurance (保険料)
    fire_text = get_table_thtd_value(soup, "保険料")
    if fire_text:
        data["fire_insurance"] = fire_text

    # Available from (入居可能日)
    avail_text = get_table_thtd_value(soup, "入居可能日")
    if avail_text:
        # Chỉ lấy "即時" nếu có, còn lại để nguyên
        if "即時" in avail_text:
            data["available_from"] = "即時"
        else:
            data["available_from"] = avail_text

    # Other initial fees (退去時費用)
    other_fees_text = get_table_thtd_value(soup, "退去時費用")
    if other_fees_text:
        fees = re.findall(r"([\d,]+)円", other_fees_text)
        if fees:
            total = sum(int(f.replace(",", "")) for f in fees)
            data["other_initial_fees"] = f"{total:,}円"
    # Facing
    facing_text = get_table_thtd_value(soup, ["向き", "方位"])
    facing_map = {
        "北": "facing_north",
        "北東": "facing_northeast",
        "東": "facing_east",
        "南東": "facing_southeast",
        "南": "facing_south",
        "南西": "facing_southwest",
        "西": "facing_west",
        "北西": "facing_northwest",
    }
    if facing_text:
        for key in facing_map.values():
            data[key] = "N"
        # Ưu tiên match key dài hơn (ví dụ: "南東" thay vì "南" + "東")
        for k in sorted(facing_map.keys(), key=len, reverse=True):
            if facing_text.strip() == k:
                data[facing_map[k]] = "Y"
                break

    # Floorplan image
    floor_img = soup.find("img", alt=re.compile("間取り"))
    if floor_img and floor_img.get("src"):
        img_url = floor_img["src"]
        if img_url.startswith("/"):
            img_url = "https://rent.tokyu-housing-lease.co.jp" + img_url
        data["floorplan"] = img_url

    # --- Images ---
    BASE_URL = "https://rent.tokyu-housing-lease.co.jp"
    thumbs = soup.select("#thumb_list ul li img")
    thumb_urls = [BASE_URL + img["src"] for img in thumbs]

    categories = soup.select(".clearfix.photo_link.room a")
    pos, img_index = 0, 1
    for cat in categories:
        text = cat.get_text(strip=True)
        if "枚" in text:
            category_name = re.sub(r"[（(]?\d+枚[)）]?", "", text).strip()
            count = int(re.search(r"(\d+)", text).group(1))

            for i in range(count):
                if pos < len(thumb_urls):
                    data[f"image_category_{img_index}"] = category_name
                    data[f"image_url_{img_index}"] = thumb_urls[pos]
                    pos += 1
                    img_index += 1

    return data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    args = parser.parse_args()

    result = parse_property(args.url)
    print(json.dumps(result, ensure_ascii=False, indent=2))
