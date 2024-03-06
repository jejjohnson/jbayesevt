import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import cartopy.crs as ccrs
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import numpy as np
from matplotlib import ticker

def plot_contour(ds, variable, vmin=None, vmax=None, cmap="bwr", num_levels=8):
    fig = plt.figure()
    fig.set_size_inches(7,5)
    ax = fig.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    loc = ticker.MaxNLocator(num_levels)
    levels = loc.tick_values(vmin, vmax)
    cbar_kwargs = {
        "fraction": 0.050, 
        "pad": 0.1, 
        "orientation": "vertical",
    }
    
    ds.plot.contourf(
        ax=ax, cmap=cmap, vmin=vmin, vmax=vmax, levels=levels,
        transform=ccrs.PlateCarree(), cbar_kwargs=cbar_kwargs
    )
    ds.plot.contour(
            ax=ax, 
            alpha=0.5, linewidths=1, cmap="black",
            levels=levels,
            # linestyles=np.where(levels >= 0, "-", "--")
            # vmin=vmin, vmax=vmax,
            # **kwargs
        )    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=0.1, color='k', alpha=1, 
                      linestyle='--')
    
    ax.set(title=variable)
    ax.coastlines(linewidth=1)
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12} 
    plt.tight_layout()
    plt.show()

    return fig, ax 


def plot_pcolormesh(ds, variable, vmin=None, vmax=None, cmap="bwr"):
    fig = plt.figure()
    fig.set_size_inches(7,5)
    ax = fig.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    cbar_kwargs = {
        "fraction": 0.050, 
        "pad": 0.1, 
        "orientation": "vertical",
    }
    
    ds.plot.pcolormesh(
        ax=ax, cmap=cmap, vmin=vmin, vmax=vmax, 
        transform=ccrs.PlateCarree(), cbar_kwargs=cbar_kwargs
    )
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=0.1, color='k', alpha=1, 
                      linestyle='--')
    
    ax.set(title=variable)
    ax.coastlines(linewidth=1)
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12} 
    plt.tight_layout()
    plt.show()

    return fig, ax 


def plot_imshow_smooth(ds, variable, vmin=None, vmax=None, cmap="bwr", num_levels=8, interpolation: str="bilinear"):
    fig = plt.figure()
    fig.set_size_inches(7,5)
    ax = fig.subplots(subplot_kw={'projection': ccrs.PlateCarree()})
    loc = ticker.MaxNLocator(num_levels)
    levels = loc.tick_values(vmin, vmax)
    cbar_kwargs = {
        "fraction": 0.050, 
        "pad": 0.1, 
        "orientation": "vertical",
    }
    
    ds.plot.imshow(
        ax=ax, cmap=cmap, vmin=vmin, vmax=vmax, #levels=levels,
        interpolation=interpolation,
        transform=ccrs.PlateCarree(), cbar_kwargs=cbar_kwargs
    )
    ds.plot.contour(
            ax=ax, 
            alpha=0.5, linewidths=1, cmap="black",
            levels=levels,
            # linestyles=np.where(levels >= 0, "-", "--")
            # vmin=vmin, vmax=vmax,
            # **kwargs
        )    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=0.1, color='k', alpha=1, 
                      linestyle='--')
    
    ax.set(title=variable)
    ax.coastlines(linewidth=1)
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12} 
    plt.tight_layout()
    plt.show()


def plot_imshow(ds, variable, vmin=None, vmax=None, cmap="bwr", num_levels=8):
    fig = plt.figure()
    fig.set_size_inches(7,5)
    ax = fig.subplots(subplot_kw={'projection': ccrs.PlateCarree()})

    cbar_kwargs = {
        "fraction": 0.050, 
        "pad": 0.1, 
        "orientation": "vertical",
    }
    
    ds.plot.imshow(
        ax=ax, cmap=cmap, vmin=vmin, vmax=vmax, #levels=levels,
        transform=ccrs.PlateCarree(), cbar_kwargs=cbar_kwargs
    )
    if num_levels is not None:
        loc = ticker.MaxNLocator(num_levels)
        levels = loc.tick_values(vmin, vmax)
        ds.plot.contour(
                ax=ax, 
                alpha=0.5, linewidths=1, cmap="black",
                levels=levels,
                # linestyles=np.where(levels >= 0, "-", "--")
                # vmin=vmin, vmax=vmax,
                # **kwargs
            )    
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=0.1, color='k', alpha=1, 
                      linestyle='--')
    
    ax.set(title=variable)
    ax.coastlines(linewidth=1)
    gl.top_labels = False
    gl.right_labels = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabel_style = {'size': 12}
    gl.ylabel_style = {'size': 12} 
    plt.tight_layout()
    plt.show()

    return fig, ax 

def interpolate_rectilinear_grid(ds, num_points: int=100, method: str="linear"):
    # interpolate
    ds = ds.interp(
        lon=np.linspace(ds.lon.values.min(), ds.lon.values.max(), num_points),
        lat=np.linspace(ds.lat.values.min(), ds.lat.values.max(), num_points),
        method="linear"
    )
    return ds
