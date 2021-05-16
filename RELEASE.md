# Release Notes

## Releases

### 0.7.2

[Released *2021-05-16*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.7.2)

- Fixed notty run of 'make update'
- Fixed login, redirect to django login
- Fixed make deploy_local

### 0.7.1
[Released *2021-05-07*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.7.1)

- Added example gallery toogle to siteconfiguration #99
- Fixed snapshot edit modal z-index, now on top
- Added debounce municipality search #92
- Added env VUE_APP_FATHOM_SITEID and VUE_APP_SNAPSHOTSTOREURL
- Changed docker setup #74
  - updated docker images
  - removed need to symlink www.local.conf
  - removed need to symlink node_modules
  - cleanup of old makefile deploy commands
  - Added DJANGO_SECRET, MAPBOX_TOKEN, MAPBOX_STYLE overwrites via .env file, see README.md
- Backend errors are now shown to the user, no longer crash the script #80
- Snapshot form validation: rule for municipality input, rule for file input #77
- Fixed Safari v-file-input #79
- Fixed update list with new snapshot #81
- Improved Snapshot upload municipality field behaviour and help button #76, #75
- Fixed empty snapshot list #72

*Upgrade notes*:
- **Breaking change**: you now need a symlink `ln -s docker-compose.dev.yml docker-compose.yml` for the local dev mode, but no other setup steps are needed anymore (see README.md)

### 0.7.1 Beta 1

- Fixed layout issues in map view on narrow viewports
- Improved language switching

### 0.7.0
[Released *2021-01-21*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.7.0)

- Added `snapshot.json` upload
- Added `snapshot.json` download in snapshot list
- Added user login via django
- Added API for snapshot upload
- Added site config for homepage_snippet and search_enabled
- Added language for homepage snippet
- Added fathom support
- Added data migration for snapshot json field to file refactor
- Added vue file upload for snapshot file
- Added frontend login page
- Added frontend snapshot editing
- Added apscheduler for screenshot generation
- Updated django image with new python package versions

*Upgrade notes*:
- Upgrading to 0.7.0 changes how snapshots are stored. The snapshot data is moved from a postgres json field to an external file. The migration is a normal django data migration and runs in the django database migration process (./manage.py migrate). The snapshot data json field will be removed in a future a release. 
- For local development symlinking the current nginx configuration is recommended (see README.md for details)

### 0.6.2
[Released *2020-11-16*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.6.2)

- Added a mock snapshot store for improved onboarding

### 0.6.1
[Released: *2020-09-03*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.6.1)

- Improved snapshot loading and switching

### 0.6.0
[Released: *2020-08-04*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.6.0)

- Added snapshot sections in workspaces and municipalities based on topic

### 0.5.1
[Released: *2020-05-27*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.5.1)

- Improved OpenGraph Support
- Improved screenshot server

### 0.5.0
[Released: *2020-05-20*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.5.0)

- Added OpenGraph support for public snapshots (rich social media links)
- Improved error messages in frontend
- Improved screenshot server
- Improved django backend

### 0.4.0
[Released: *2020-05-11*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.4.0)

- Added PNG downloads
- Added screenshot server
- Added Django and Vue tests

### 0.3.1
[Released: *2020-04-09*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.3.1)
[Sprint: 4 "Out of the Box"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+4%3A+Out+of+the+box)

- Small fixes

### 0.3.0 "Out of the Box"
[Released: *2020-04-09*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.3.0)
[Sprint: 4 "Out of the Box"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+4%3A+Out+of+the+box)

- Workspace support
- Improved layouts
- Improved deployment
- Improved JSON editor in Django-Admin
- Experimental branch: automatic screenshot generator

### 0.2.1
[Released: *2020-03-16*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.2.1)
[Sprint: 3 "Hello World"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+3%3A+Hello+world)

- Legend is now using SVG rendering
- Small fixes

### 0.2.0 "Hello World"
[Released: *2020-03-11*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.2.0)
[Sprint: 3 "Hello World"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+3%3A+Hello+world)

- SnapshotView support according to [Gemeindescan Datapackage Specification](https://bitbucket.org/cividi/gemeindescan-sample/)
- Based on Leaflet and [Simple Style GeoJSON](https://github.com/mapbox/simplestyle-spec)
- Support for [Simple Style GeoJSON](https://github.com/mapbox/simplestyle-spec) and Leaflet Circles
- Support for Legends
- GeoDjango added

### 0.1.2
[Released: *2020-02-20*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.1.2)
[Sprint: 2 "Map Space"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+2%3A+Map+space)

- Multilanguage support via [`vue-i18n`](https://github.com/kazupon/vue-i18n)
- Improved docker setup
- Experimental: snapshot view

### 0.1.1
[Released: *2020-02-13*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.1.1)
[Sprint: 2 "Map Space"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+2%3A+Map+space)

- Static content updates

### 0.1.0
[Released: *2020-02-06*](https://github.com/cividi/spatial-data-package-platform/releases/tag/0.1.0)
[Sprint: 0 "Project Setup" + Sprint 1 "Splash Down"](https://bitbucket.org/cividi/gemeindescan-webui/issues?milestone=SP+1%3A+Splash+down&milestone=SP+0%3A+Project+setup)

- Initial version
- Django + Graphene + GraphQL + Vue setup

## See also

In [issue 1](https://bitbucket.org/cividi/gemeindescan-webui/issues/1) you can find an overview of the tech stack, and [issue 2](https://bitbucket.org/cividi/gemeindescan-webui/issues/1) for more general background.
