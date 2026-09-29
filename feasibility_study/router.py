SECTOR_FILES = {
    "saas": "references/sectors/digital-services.md",
    "enterprise software": "references/sectors/digital-services.md",
    "marketplace": "references/sectors/digital-services.md",
    "ecommerce": "references/sectors/digital-services.md",
    "e-commerce": "references/sectors/digital-services.md",
    "fintech": "references/sectors/digital-services.md",
    "professional services": "references/sectors/digital-services.md",
    "managed services": "references/sectors/digital-services.md",
    "hospital": "references/sectors/healthcare-life-sciences.md",
    "clinic": "references/sectors/healthcare-life-sciences.md",
    "laboratory": "references/sectors/healthcare-life-sciences.md",
    "medical device": "references/sectors/healthcare-life-sciences.md",
    "ivd": "references/sectors/healthcare-life-sciences.md",
    "pharma": "references/sectors/healthcare-life-sciences.md",
    "biotech": "references/sectors/healthcare-life-sciences.md",
    "digital health": "references/sectors/healthcare-life-sciences.md",
    "manufacturing": "references/sectors/industrial-resources.md",
    "factory": "references/sectors/industrial-resources.md",
    "food manufacturing": "references/sectors/industrial-resources.md",
    "agriculture": "references/sectors/industrial-resources.md",
    "livestock": "references/sectors/industrial-resources.md",
    "aquaculture": "references/sectors/industrial-resources.md",
    "energy": "references/sectors/industrial-resources.md",
    "renewables": "references/sectors/industrial-resources.md",
    "mining": "references/sectors/industrial-resources.md",
    "quarrying": "references/sectors/industrial-resources.md",
    "real estate": "references/sectors/asset-consumer.md",
    "hotel": "references/sectors/asset-consumer.md",
    "hospitality": "references/sectors/asset-consumer.md",
    "restaurant": "references/sectors/asset-consumer.md",
    "cafe": "references/sectors/asset-consumer.md",
    "education": "references/sectors/asset-consumer.md",
    "training": "references/sectors/asset-consumer.md",
    "logistics": "references/sectors/asset-consumer.md",
    "warehouse": "references/sectors/asset-consumer.md",
    "ppp": "references/sectors/asset-consumer.md",
    "infrastructure": "references/sectors/asset-consumer.md",
    "retail": "references/sectors/asset-consumer.md",
    "wholesale": "references/sectors/asset-consumer.md",
    "franchise": "references/sectors/asset-consumer.md",
}

def route_sector(sector, subsector):
    text = f"{sector} {subsector}".strip().lower()
    matches = []
    for key, path in SECTOR_FILES.items():
        if key in text and path not in matches:
            matches.append(path)
    return matches

def routing_plan(profile):
    required = ["project_name","sector","subsector","business_model","jurisdiction","stage","study_mode","currency"]
    missing = [x for x in required if not str(profile.get(x,"")).strip()]
    if missing:
        raise ValueError("missing project-profile fields: " + ", ".join(missing))
    sector_files = route_sector(profile["sector"], profile["subsector"])
    return {
        "core": [
            "references/core/methodology.md",
            "references/core/sector-routing.md",
            "references/core/financial-model-standard.md",
            "references/core/artifact-output-standard.md",
        ],
        "sector_files": sector_files,
        "dynamic_sector_pack_required": not bool(sector_files),
        "jurisdiction_hint": "references/jurisdictions/saudi-arabia-v2.md"
            if "saudi" in profile["jurisdiction"].lower() or "السعود" in profile["jurisdiction"]
            else None,
    }
