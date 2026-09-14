"""Validate the documented skills.sh format and our catalog coverage policy."""


def grouping_errors(config, names):
    errors = []
    if not isinstance(config, dict):
        return ["skills.sh.json: expected an object"]
    if config.get("notGrouped", "bottom") not in ("top", "bottom"):
        errors.append("skills.sh.json: notGrouped must be top or bottom")
    if "$schema" in config and not isinstance(config["$schema"], str):
        errors.append("skills.sh.json: $schema must be a string")
    unknown = set(config) - {"$schema", "notGrouped", "groupings"}
    if unknown:
        errors.append(f"skills.sh.json: unknown fields {sorted(unknown)}")
    groups = config.get("groupings")
    if not isinstance(groups, list) or not 1 <= len(groups) <= 50:
        return errors + ["skills.sh.json: groupings must contain 1–50 groups"]
    seen = set()
    titles = set()
    for index, group in enumerate(groups):
        label = f"skills.sh.json: group {index + 1}"
        if not isinstance(group, dict):
            errors.append(f"{label}: expected an object")
            continue
        unknown = set(group) - {"title", "description", "skills"}
        if unknown:
            errors.append(f"{label}: unknown fields {sorted(unknown)}")
        title = group.get("title")
        if not isinstance(title, str) or not title.strip():
            errors.append(f"{label}: title must be non-empty")
        elif title.strip().casefold() in titles:
            errors.append(f"{label}: duplicate title {title!r}")
        else:
            titles.add(title.strip().casefold())
        if "description" in group and not isinstance(group["description"], str):
            errors.append(f"{label}: description must be a string")
        skills = group.get("skills")
        if not isinstance(skills, list) or not 1 <= len(skills) <= 500:
            errors.append(f"{label}: skills must contain 1–500 names")
            continue
        for name in skills:
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{label}: skill names must be non-empty strings")
                continue
            if name not in names:
                errors.append(f"{label}: unknown source skill {name!r}")
            if name in seen:
                errors.append(f"{label}: skill {name!r} appears more than once")
            seen.add(name)
    missing = set(names) - seen
    if missing:
        errors.append(f"skills.sh.json: ungrouped source skills {sorted(missing)}")
    return errors
