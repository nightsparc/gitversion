_cpp_format = """
// ---------------------------------------------------
// This file is autogenerated by git-version.
// DO NOT MODIFY!
// ---------------------------------------------------

#pragma once
#ifndef __GITVERSIONBUILDER__VERSION_H__
#define __GITVERSIONBUILDER__VERSION_H__

namespace version {
  constexpr const char *VERSION_STRING = "%s";
  constexpr const char *GIT_TAG_NAME = "%s";
  constexpr const unsigned int GIT_COMMITS_SINCE_TAG = %d;
  constexpr const char *GIT_COMMIT_ID = "%s";
}

#endif
"""

_python_format = """
# ---------------------------------------------------
# This file is autogenerated by git-version.
# DO NOT MODIFY!
# ---------------------------------------------------

VERSION_STRING = "%s"
GIT_TAG_NAME = "%s"
GIT_COMMITS_SINCE_TAG = %d
GIT_COMMIT_ID = "%s"
"""


def _output(version_info, format):
    return format % (
        version_info.version_string, version_info.git_tag_name, version_info.git_commits_since_tag,
        version_info.git_commit_id)


def to_cpp(version_info):
    return _output(version_info, _cpp_format)


def to_python(version_info):
    return _output(version_info, _python_format)
