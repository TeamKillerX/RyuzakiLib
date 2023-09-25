/**
#!/usr/bin/env javascript
# -*- coding: utf-8 -*-
# Copyright 2020-2023 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
**/

const { Bot, InlineKeyboard } = require("grammy");
// const { BOT_TOKEN } = require('./env.js')
const axios = require("axios");

const bot = new Bot("your bot token here");

const randydev = new InlineKeyboard().url("channel Projects", "https://t.me/RendyProjects");
const photo = "https://telegra.ph/file/059480066c992e16c0915.jpg"

const Commands = `
Welcome to Bots testing (JavaScript)

/github > get github username
/ipcheck > tracking ip address

• features coming soon
• Developer by @xtdevs
`;

bot.command("start", async (ctx) => {
    await ctx.replyWithPhoto(photo,{
        caption: Commands,
        reply_to_message_id: ctx.msg.message_id,
        reply_markup: randydev,
    });
});

bot.command("github", async (ctx) => {
    const username = ctx.message.text.split(" ")[1];

    if (!username) {
        await ctx.reply("Please provide a GitHub username.");
        return;
    }

    const url = `https://private.randydev.my.id/github?username=${username}`;

    try {
        const response = await axios.get(url);

        const data = response.data;
        const photo = data.randydev.avatar;
        const results = data.randydev.results;

        if (photo && results) {
            await ctx.replyWithPhoto(photo, {
                caption: results,
                reply_to_message_id: ctx.msg.message_id,
                parse_mode: 'Markdown',
            });
        } else {
            await ctx.reply("GitHub user not found.");
        }
    } catch (error) {
        console.error(error);
        await ctx.reply("An error occurred while fetching GitHub data.");
    }
});

bot.command("ipcheck", async (ctx) => {
    const ipaddres = ctx.message.text.split(" ")[1];

    if (!ipaddres) {
        await ctx.reply("Please give ip address");
        return;
    }

    const url = `https://private.randydev.my.id/ipcheck?ip_address=${ipaddres}`;

    try {
        const response = await axios.get(url);

        const data = response.data;
        const region = data.region_name;
        const language_code = data.country_code;
        const zip_code = data.zip_code;
        const as = data.as;

        if (region && language_code && zip_code && as) {
            await ctx.reply(`<b>Region Name</b>: <code>${region}</code>\n<b>Language Code</b>: <code>${region}</code>\n<b>AS</b>: <code>${as}</code>`, {
                reply_to_message_id: ctx.msg.message_id,
                parse_mode: 'Html',
                reply_markup: randydev,
            });
        } else {
            await ctx.reply("ip address not found.");
        }
    } catch (error) {
        console.error(error);
        await ctx.reply("An error occurred while fetching ip address.");
    }
});

bot.start();
