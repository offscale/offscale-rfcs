#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os import listdir, path, remove

import genson
import yaml

schemas_dir = path.dirname(path.abspath(__file__))


def as_dict(fname):
    with open(fname) as f:
        return fname, yaml.load(f)


def to_schema(fname, *ds):
    s = genson.Schema()
    s.add_schema(
        {
            "type": "object",
            "properties": {},
            "title": (lambda fname: fname[: fname.find(".")])(path.basename(fname)),
        }
    )
    s.schema_uri = "http://json-schema.org/draft-04/schema"
    for d in ds:
        s.add_object(d)
    with open(path.join(schemas_dir, fname.replace(".yml", ".schema.json")), "wt") as f:
        f.write(s.to_json(indent=4))


def yml_out(fname):
    with open(fname) as f0, open(fname.replace(".json", ".yml"), "wt") as f1:
        yaml.safe_dump(json.load(f0), f1, default_flow_style=False)


def seq1_endswith0(sequence, endswith):
    return (
        two_d[1] for two_d in sequence if path.basename(two_d[0]).endswith(endswith)
    )


if __name__ == "__main__":
    tuple(
        remove(path.join(schemas_dir, f))
        for f in listdir(schemas_dir)
        if f.endswith(".json")
    )
    ymls = tuple(
        as_dict(path.join(schemas_dir, f))
        for f in listdir(schemas_dir)
        if f.endswith(".yml")
    )
    to_schema("service.schema.json", *seq1_endswith0(ymls, "service.yml"))
    to_schema("package.schema.json", *seq1_endswith0(ymls, "service.yml"))
    to_schema("iaas.schema.json", *seq1_endswith0(ymls, "iaas.yml"))
    tuple(
        yml_out(path.join(schemas_dir, f))
        for f in listdir(schemas_dir)
        if f.endswith(".json")
    )
