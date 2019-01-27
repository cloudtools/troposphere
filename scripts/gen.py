from troposphere_gen.specification import Specification
from troposphere_gen.generator import Generator
from troposphere_gen.policy import *
from troposphere_gen.policy import cc_to_sc

import json

from collections import OrderedDict


def generate(specificationfile: str, outdir: str, policy: Policy):
    with open(specificationfile, "r") as f:
        specdata = json.load(f, object_pairs_hook=OrderedDict)

    spec = Specification(specdata)
    gen = Generator(spec)

    for name, module in gen.modules.items():
        with open(outdir + cc_to_sc(name) + ".py", "w") as f:
            f.write(policy.module_head_format(module, spec))
            f.write(policy.after_import())

            for name, cd in module.properties.items():
                f.write(policy.class_format(cd))
                f.write(policy.between_class())

            for name, cd in module.resources.items():
                f.write(policy.class_format(cd))
                f.write(policy.between_class())


if __name__ == "__main__":
    generate("CloudFormationResourceSpecification.json", "build/2.7/", Policy_2_7())
    generate("CloudFormationResourceSpecification.json", "build/3.7/", Policy_3_7())
