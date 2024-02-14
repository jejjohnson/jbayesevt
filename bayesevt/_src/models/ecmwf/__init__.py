# from functools import cached_property
# import climetlab as cml


# class FileInput:
#     def __init__(self, owner, file, **kwargs):
#         self.file = file
#         self.owner = owner

#     @cached_property
#     def fields_sfc(self):
#         return self.all_fields.sel(levtype="sfc")

#     @cached_property
#     def fields_pl(self):
#         return self.all_fields.sel(levtype="pl")

#     @cached_property
#     def fields_ml(self):
#         return self.all_fields.sel(levtype="ml")

#     @cached_property
#     def all_fields(self):
#         raise NotImplementedError()
#         # return cml.load_source("file", self.file)

import ai_models
import climetlab as cml

from dataclasses import dataclass
from functools import cached_property

@dataclass
class Arguments:
    model: str = "fourcastnetv2-small"
    model_version: str = "latest"
    output: str = "file"
    download_assets: bool = True
    verbose: int = 0
    date: str = 20210801
    time: int = 12
    assets: str = "/home/juanjohn/data/forecasters/ai_models"
    assets_sub_directory: str = "fourcastnetv2-small"
    path: str = "./"
    lead_time: int = 6
    only_gpu: bool = False

args = Arguments()


class CustomFileInput:
    def __init__(self, owner, pl_file, sfc_file, **kwargs):
        self.pl_file = pl_file
        self.sfc_file = sfc_file
        self.owner = owner

    @cached_property
    def fields_sfc(self):
        return cml.load_source("file", self.sfc_file)

    @cached_property
    def fields_pl(self):
        return cml.load_source("file", self.pl_file)

    @cached_property
    def fields_ml(self):
        raise NotImplementedError()

    @cached_property
    def all_fields(self):
        return self.fields_sfc + self.fields_pl
    

sfc_file = "/pool/usuarios/juanjohn/ai_models/data/era5/surface_fourcastnet.grib"
pl_file = "/pool/usuarios/juanjohn/ai_models/data/era5/levels_fourcastnet.grib"

file_input = CustomFileInput(None, sfc_file, pl_file)


from ai_models_fourcastnetv2.model import FourCastNetv2
from ai_models.model import ArchiveCollector
from collections import defaultdict
from loguru import logger
import os
from ai_models.outputs import get_output
import time

class CustomModel(FourCastNetv2):
    def __init__(self, **kwargs):

        self.input = file_input #get_input(input, self, **kwargs)
        self.output = get_output(name="file", owner=self, metadata={}, **kwargs)

        print(self.output)
        print(type(self.output))
    
        for k, v in kwargs.items():
            setattr(self, k, v)

        # # We need to call it to initialise the default args
        # args = self.parse_model_args(self.model_args)
        # if args:
        #     for k, v in vars(args).items():
        #         setattr(self, k, v)

        if self.assets_sub_directory:
            if self.assets_extra_dir is not None:
                self.assets += self.assets_extra_dir

        logger.debug("Asset directory is %s", self.assets)

        try:
            # For CliMetLab, when date=-1
            self.date = int(self.date)
        except ValueError:
            pass

        # self.download_assets(**kwargs)

        self.archiving = defaultdict(ArchiveCollector)
        self.created = time.time()

        self.n_lat = 721
        self.n_lon = 1440
        self.hour_steps = 6

        self.backbone_channels = len(self.ordering)

        self.checkpoint_path = os.path.join(self.assets, "weights.tar")


model = CustomModel(**vars(args))

print("here!")

model.run()