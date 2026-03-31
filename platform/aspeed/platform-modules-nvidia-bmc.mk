# NVIDIA BMC Platform modules
#
# NOTE: When adding more hardware variants (e.g., ast2800), use add_extra_package:
#   ASPEED_NVIDIA_AST2800_BMC_PLATFORM_MODULE = sonic-platform-aspeed-nvidia-ast2800-bmc_1.0_arm64.deb
#   $(ASPEED_NVIDIA_AST2800_BMC_PLATFORM_MODULE)_PLATFORM = arm64-aspeed_nvidia_ast2800_bmc-r0
#   $(eval $(call add_extra_package,$(ASPEED_NVIDIA_AST2700_BMC_PLATFORM_MODULE),$(ASPEED_NVIDIA_AST2800_BMC_PLATFORM_MODULE)))

ASPEED_NVIDIA_AST2700_BMC_PLATFORM_MODULE = sonic-platform-aspeed-nvidia-ast2700-bmc_1.0_arm64.deb
$(ASPEED_NVIDIA_AST2700_BMC_PLATFORM_MODULE)_SRC_PATH = $(PLATFORM_PATH)/sonic-platform-modules-nvidia-bmc
$(ASPEED_NVIDIA_AST2700_BMC_PLATFORM_MODULE)_PLATFORM = arm64-aspeed_nvidia_ast2700_bmc-r0
SONIC_DPKG_DEBS += $(ASPEED_NVIDIA_AST2700_BMC_PLATFORM_MODULE)
