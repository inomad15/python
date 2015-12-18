//
// Copyright (C) 2011-15 DyND Developers
// BSD 2-Clause License, see LICENSE.txt
//

#pragma once

#include <dynd/func/callable.hpp>

namespace dynd {
namespace nd {

  extern DYND_API struct min : declfunc<min> {
    static DYND_API callable make();
  } min;

} // namespace dynd::nd
} // namespace dynd
