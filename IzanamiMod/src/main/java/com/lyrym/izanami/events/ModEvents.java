package com.lyrym.izanami.events;

import com.lyrym.izanami.Izanami;
import net.minecraft.world.entity.player.Player;
import net.minecraftforge.event.entity.living.LivingDamageEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.common.Mod;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

@Mod.EventBusSubscriber(modid=Izanami.MOD_ID)
public class ModEvents {
    private static Logger logger = LogManager.getLogger();
    @SubscribeEvent
    public static void HealthListener(LivingDamageEvent event){
        logger.info("1");

        if(!event.getEntity().level.isClientSide()){
            logger.info("2");

            if(event.getEntity() instanceof Player){
                Player player = ((Player) event.getEntity());
                System.out.println(player.getHealth());
            }
        }

    }

}
